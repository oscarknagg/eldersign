from abc import ABC, abstractmethod
from typing import List, Type, TypeVar
import logging
import random

from eldersign.core import AbstractEffect, AdventureEffect, Investigator, InvestigatorEffect
from eldersign.symbol import Terror
from eldersign.item import Item


log = logging.getLogger(__name__)
T = TypeVar('T')


class EffectChoice(AbstractEffect):
    def __init__(self, effects: List[AbstractEffect]):
        self.effects = effects

    def apply_effect(self, *args, **kwargs):
        # TODO: policy to choose
        available_effects = [effect for effect in self.effects if self.check_requirements(*args, **kwargs)]
        effect = random.choice(available_effects)
        effect(*args, **kwargs)


class InvestigatorEffectChoice(InvestigatorEffect):
    def __init__(self, effects: List[InvestigatorEffect]):
        self.effects = effects

    def apply_effect(self, investigator: Investigator):
        # TODO: policy to choose
        available_effects = [effect for effect in self.effects if self.check_requirements(investigator)]
        effect = random.choice(available_effects)
        effect(investigator)


def union_effects(effects: List[T]) -> T:
    """I don't know if this will work but its cool."""
    class _UnionEffect(type(effects[0])):
        def __init__(self, _effects: List[T]):
            self._effects = _effects

        def apply_effect(self, *args, **kwargs):
            for effect in self._effects:
                effect(*args, **kwargs)

    return _UnionEffect(_effects=effects)


class UnionEffect(AbstractEffect):
    def __init__(self, effects: List[AbstractEffect]):
        self.effects = effects

    def apply_effect(self, *args, **kwargs):
        for effect in self.effects:
            effect(*args, **kwargs)


class AddDoomToken(AdventureEffect):
    def __init__(self, value: int):
        self.value = value

    def apply_effect(self, adventure_attempt, eldersign):
        eldersign.ancient_one.doom_tokens = max(0, eldersign.ancient_one.doom_tokens-self.value)


class AddElderSign(AdventureEffect):
    def __init__(self, value: int):
        self.value = value

    def apply_effect(self, adventure_attempt, eldersign):
        eldersign.ancient_one.elder_signs = max(0, eldersign.ancient_one.elder_signs-self.value)


class InvestigatorAdventureEffect(AdventureEffect):
    def __init__(self, effect: InvestigatorEffect):
        self.effect = effect

    def apply_effect(self, adventure_attempt, eldersign):
        self.effect(adventure_attempt.character)


class EachInvestigator(AdventureEffect):
    def __init__(self, effect: InvestigatorEffect):
        self.effect = effect

    def apply_effect(self, adventure_attempt, eldersign):
        for investigator in eldersign.characters:
            self.effect(investigator)


class AddHealth(InvestigatorEffect):
    def __init__(self, value: int):
        self.value = value

    def apply_effect(self, investigator: Investigator):
        investigator.health -= self.value


class AddSanity(InvestigatorEffect):
    def __init__(self, value: int):
        self.value = value

    def apply_effect(self, investigator: Investigator):
        investigator.sanity -= self.value


class Curse(InvestigatorEffect):
    def apply_effect(self, investigator: 'Investigator'):
        if investigator.blessed:
            investigator.blessed = False
        else:
            investigator.cursed = True


class Bless(InvestigatorEffect):
    def apply_effect(self, investigator: 'Investigator'):
        if investigator.cursed:
            investigator.cursed = False
        else:
            investigator.blessed = True


class DiscardAllTerrorDice(AdventureEffect):
    def apply_effect(self, adventure_attempt, eldersign):
        dice_pool = adventure_attempt.dice_pool
        num_removed = 0
        for d in dice_pool:
            if d.symbol == Terror():
                dice_pool.remove(d)
                num_removed += 1

        log.debug("{}: Discarding {} dice".format(self.__class__.__name__, num_removed))


class MonsterAppearsHere(AdventureEffect):
    def apply_effect(self, adventure_attempt, eldersign):
        pass  # Monsters not implemented yet


class MonsterAppears(AdventureEffect):
    def apply_effect(self, adventure_attempt, eldersign):
        pass  # Monsters not implemented yet


class ThreeDoomsIfAnyMonster(AdventureEffect):
    def apply_effect(self, adventure_attempt, eldersign):
        # approximate with +1 doom
        # TODO: implement
        eldersign.ancient_one.doom_tokens += 1


class MonsterAppearsOnEveryMonsterTask(AdventureEffect):
    def apply_effect(self, adventure_attempt, eldersign):
        pass  # Monsters not implemented yet


class ImmediatelyFail(AdventureEffect):
    def apply_effect(self, adventure_attempt, eldersign):
        adventure_attempt.force_failed = True


class AddItem(AdventureEffect):
    def __init__(self, item_type: Type[Item], amount: int = 1):
        self.item_type = item_type
        assert amount != 0
        self.amount = 1

    def apply_effect(self, adventure_attempt, eldersign):
        if self.amount > 0:
            for i in range(self.amount):
                drawn_item = eldersign.decks[self.item_type].draw()
                adventure_attempt.character.items += drawn_item
        else:
            to_remove = []
            for item in adventure_attempt.character.items:
                if isinstance(item, self.item_type):
                    to_remove.append(item)

            for i in to_remove:
                adventure_attempt.character.items.remove(i)

            log.debug("Removed {} items from {}".format(len(to_remove), adventure_attempt.character))


class OpenGate(AdventureEffect):
    def apply_effect(self, adventure_attempt, eldersign):
        pass


class SpendTrophies(InvestigatorEffect):
    def __init__(self, value: int):
        self.value = value

    def apply_effect(self, investigator: 'Investigator'):
        if any(t.trophy_value == self.value for t in investigator.trophies):
            for t in investigator.trophies:
                if t.trophy_value == self.value:
                    investigator.trophies.remove(t)
                    return

        num_spent = 0
        to_remove = []
        for t in sorted(investigator.trophies, key=lambda t: t.trophy_value):
            num_spent += t.trophy_value
            to_remove += t

            if num_spent >= self.value:
                break

        for t in to_remove:
            investigator.trophies.remove(t)

    def check_requirements(self, investigator: 'Investigator') -> bool:
        return sum(t.trophy_value for t in investigator.trophies) >= self.value


class NotImplementedEffect(AdventureEffect):
    def __init__(self, text: str):
        """Just for documenting not-implemented effects"""
        self.text = text

    def apply_effect(self, adventure_attempt, eldersign):
        pass
