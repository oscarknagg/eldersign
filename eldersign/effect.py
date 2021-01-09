from abc import ABC, abstractmethod
from typing import List, Type
import logging
import random

from eldersign.core import AdventureEffect, Character
from eldersign.symbol import Terror
from eldersign.item import Item


log = logging.getLogger(__name__)


class EffectChoice(AdventureEffect):
    def __init__(self, effects: List[AdventureEffect]):
        self.effects = effects

    def __call__(self, adventure_attempt, eldersign):
        # TODO: policy to choose
        effect = random.choice(self.effects)
        effect(adventure_attempt, eldersign)


class UnionEffect(AdventureEffect):
    def __init__(self, effects: List[AdventureEffect]):
        self.effects = effects

    def __call__(self, adventure_attempt, eldersign):
        for effect in self.effects:
            effect(adventure_attempt, eldersign)


class DoomTokenEffect(AdventureEffect):
    def __init__(self, value: int):
        self.value = value

    def __call__(self, adventure_attempt, eldersign):
        eldersign.ancient_one.doom_tokens = max(0, eldersign.ancient_one.doom_tokens-self.value)


class ElderSignEffect(AdventureEffect):
    def __init__(self, value: int):
        self.value = value

    def __call__(self, adventure_attempt, eldersign):
        eldersign.ancient_one.elder_signs = max(0, eldersign.ancient_one.elder_signs-self.value)


class HealthEffect(AdventureEffect):
    def __init__(self, value: int):
        self.value = value

    def __call__(self, adventure_attempt, eldersign):
        adventure_attempt.character.health -= self.value


class SanityEffect(AdventureEffect):
    def __init__(self, value: int):
        self.value = value

    def __call__(self, adventure_attempt, eldersign):
        adventure_attempt.character.sanity -= self.value


class DiscardAllTerrorDice(AdventureEffect):
    def __call__(self, adventure_attempt, eldersign):
        dice_pool = adventure_attempt.dice_pool
        num_removed = 0
        for d in dice_pool:
            if d.symbol == Terror():
                dice_pool.remove(d)
                num_removed += 1

        log.debug("{}: Discarding {} dice".format(self.__class__.__name__, num_removed))


class MonsterAppearsHere(AdventureEffect):
    def __call__(self, adventure_attempt, eldersign):
        pass  # Monsters not implemented yet


class MonsterAppears(AdventureEffect):
    def __call__(self, adventure_attempt, eldersign):
        pass  # Monsters not implemented yet


class ImmediatelyFail(AdventureEffect):
    def __call__(self, adventure_attempt, eldersign):
        adventure_attempt.force_failed = True


class ItemReward(AdventureEffect):
    def __init__(self, item_type: Type[Item]):
        self.item_type = item_type

    def __call__(self, adventure_attempt, eldersign):
        drawn_item = eldersign.decks[self.item_type].draw()
        adventure_attempt.character.items += drawn_item


class NotImplementedEffect(AdventureEffect):
    def __init__(self, text: str):
        """Just for documenting not-implemented effects"""
        self.text = text

    def __call__(self, adventure_attempt, eldersign):
        pass
