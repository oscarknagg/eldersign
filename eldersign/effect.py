from abc import ABC, abstractmethod
from typing import List
import random

from eldersign.character import Character
from eldersign.core import AdventureEffect


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
    def __call__(self, adventure_attempt, eldersign):
        eldersign.ancient_one.doom_tokens += 1


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

