from typing import List, Type, TypeVar, Optional, Union
import logging
import random

from eldersign.core import AbstractEffect, AdventureEffect, Investigator, InvestigatorEffect, Board, TrophyMixin
from eldersign.symbol import Terror
from eldersign.item import Item


log = logging.getLogger(__name__)
T = TypeVar('T')


class InvestigatorAttemptingAdventure(AdventureEffect):
    def __init__(self, effect: InvestigatorEffect):
        self.effect = effect

    def apply_effect(self, adventure_atttempt, eldersign: Board):
        self.effect(adventure_atttempt.investigator)


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


# def union_effects(effects: List[T]) -> T:
#     """I don't know if this will work but its cool."""
#     class _UnionEffect(type(effects[0])):
#         def __init__(self, _effects: List[T]):
#             self._effects = _effects
#
#         def apply_effect(self, *args, **kwargs):
#             for effect in self._effects:
#                 effect(*args, **kwargs)
#
#     return _UnionEffect(_effects=effects)


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
        eldersign.ancient_one.doom_tokens = max(0, eldersign.ancient_one.doom_tokens+self.value)


class AddElderSign(AdventureEffect):
    def __init__(self, value: int):
        self.value = value

    def apply_effect(self, adventure_attempt, eldersign):
        eldersign.ancient_one.elder_signs = max(0, eldersign.ancient_one.elder_signs+self.value)


class InvestigatorAdventureEffect(AdventureEffect):
    def __init__(self, effect: InvestigatorEffect):
        self.effect = effect

    def apply_effect(self, adventure_attempt, eldersign):
        self.effect(adventure_attempt.investigator)


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
        investigator.health += self.value


class ItsGotMe(InvestigatorEffect):
    """Specifically for the It's Got Me adventure"""
    def apply_effect(self, investigator: 'Investigator'):
        dice_roll = random.randint(1, 6)
        if dice_roll <= 3:
            investigator.health -= dice_roll


class AddSanity(InvestigatorEffect):
    def __init__(self, value: int):
        self.value = value

    def apply_effect(self, investigator: Investigator):
        investigator.sanity += self.value


class SetHealthSanity(InvestigatorEffect):
    def __init__(self, health: Optional[int] = None, sanity: Optional[int] = None):
        self.health = health
        self.sanity = sanity

    def apply_effect(self, investigator: Investigator):
        if self.health:
            investigator.health = self.health

        if self.sanity:
            investigator.sanity = self.sanity


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
        eldersign.num_monsters += 1


class MonsterAppears(AdventureEffect):
    def __init__(self, num_monsters: int = 1):
        self.num_monsters = num_monsters

    def apply_effect(self, adventure_attempt, eldersign):
        eldersign.num_monsters += self.num_monsters


class ThreeDoomsIfAnyMonster(AdventureEffect):
    def apply_effect(self, adventure_attempt, eldersign):
        # approximate with +1 doom
        # TODO: implement
        eldersign.ancient_one.doom_tokens += 1


class MonsterAppearsOnEveryMonsterTask(AdventureEffect):
    def apply_effect(self, adventure_attempt, eldersign):
        # Approximate with +2
        eldersign.num_monsters += 2


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
                adventure_attempt.investigator.items.append(drawn_item)
        else:
            to_remove = []
            for item in adventure_attempt.investigator.items:
                if isinstance(item, self.item_type):
                    to_remove.append(item)

            for i in to_remove:
                adventure_attempt.investigator.items.remove(i)

            log.debug("Removed {} items from {}".format(len(to_remove), adventure_attempt.investigator))


class OpenGate(AdventureEffect):
    def apply_effect(self, adventure_attempt, eldersign):
        pass


class AddTime(AdventureEffect):
    def __init__(self, value: int):
        self.value = value

    def apply_effect(self, adventure_attempt, eldersign):
        for i in range(self.value):
            eldersign.clock.add_hours(3)


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
            to_remove.append(t)

            if num_spent >= self.value:
                break

        for t in to_remove:
            investigator.trophies.remove(t)

    def check_requirements(self, investigator: 'Investigator') -> bool:
        return sum(t.trophy_value for t in investigator.trophies) >= self.value


class AddTrophies(InvestigatorEffect):
    def __init__(self, values: Union[int, List[int]]):
        self.values = values

    def apply_effect(self, investigator: 'Investigator'):
        for v in self.values:
            investigator.trophies.append(TrophyMixin(v))


class NotImplementedEffect(AdventureEffect):
    def __init__(self, text: str):
        """Just for documenting not-implemented effects"""
        self.text = text

    def apply_effect(self, adventure_attempt, eldersign):
        pass
