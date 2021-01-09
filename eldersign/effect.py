from abc import ABC, abstractmethod
from typing import List, Type
import logging
import random

from eldersign.core import AbstractEffect, AdventureEffect, Investigator, InvestigatorEffect
from eldersign.symbol import Terror
from eldersign.item import Item


log = logging.getLogger(__name__)


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


class UnionEffect(AbstractEffect):
    def __init__(self, effects: List[AbstractEffect]):
        self.effects = effects

    def apply_effect(self, *args, **kwargs):
        for effect in self.effects:
            effect(*args, **kwargs)


class DoomTokenEffect(AdventureEffect):
    def __init__(self, value: int):
        self.value = value

    def apply_effect(self, adventure_attempt, eldersign):
        eldersign.ancient_one.doom_tokens = max(0, eldersign.ancient_one.doom_tokens-self.value)


class ElderSignEffect(AdventureEffect):
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


class HealthEffect(InvestigatorEffect):
    def __init__(self, value: int):
        self.value = value

    def apply_effect(self, investigator: Investigator):
        investigator.health -= self.value


class SanityEffect(InvestigatorEffect):
    def __init__(self, value: int):
        self.value = value

    def apply_effect(self, investigator: Investigator):
        investigator.sanity -= self.value


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


class MonsterAppearsOnEveryMonsterTask(AdventureEffect):
    def apply_effect(self, adventure_attempt, eldersign):
        pass  # Monsters not implemented yet


class ImmediatelyFail(AdventureEffect):
    def apply_effect(self, adventure_attempt, eldersign):
        adventure_attempt.force_failed = True


class ItemReward(AdventureEffect):
    def __init__(self, item_type: Type[Item]):
        self.item_type = item_type

    def apply_effect(self, adventure_attempt, eldersign):
        drawn_item = eldersign.decks[self.item_type].draw()
        adventure_attempt.character.items += drawn_item


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
