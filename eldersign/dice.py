import random
from abc import ABC, abstractmethod
from typing import List

from eldersign.symbol import Symbol, Investigation, Terror, Skull, Scroll, Wildcard


class Dice(ABC):
    symbol: Symbol  # The symbol currently showing on the dice
    colour: str

    @abstractmethod
    def roll(self):
        raise NotImplementedError

    def __repr__(self):
        return '{}({})'.format(self.colour, self.symbol)


class GreenDice(Dice):
    colour = 'Green'

    def roll(self):
        result = random.randint(1, 6)
        if result in (1, 2, 3):
            self.symbol = Investigation(result)
        elif result == 4:
            self.symbol = Scroll()
        elif result == 5:
            self.symbol = Skull()
        else:
            self.symbol = Terror()


class RedDice(Dice):
    colour = 'Red'

    def roll(self):
        result = random.randint(1, 6)
        if result in (1, 2, 3):
            self.symbol = Investigation(result+1)
        elif result == 4:
            self.symbol = Scroll()
        elif result == 5:
            self.symbol = Skull()
        else:
            self.symbol = Wildcard()


class YellowDice(Dice):
    colour = 'Yellow'

    def roll(self):
        result = random.randint(1, 6)
        if result in (1, 2, 3, 4):
            self.symbol = Investigation(result)
        elif result == 5:
            self.symbol = Scroll()
        else:
            self.symbol = Skull()


class DicePool:
    def __init__(self, dice: List[Dice]):
        self.dice = dice

    def __len__(self):
        return len(self.dice)

    def roll(self):
        for dice in self.dice:
            dice.roll()

    def discard(self) -> Dice:
        for i, dice in enumerate(self.dice):
            if isinstance(dice, GreenDice):
                # Get rid of green first
                return self.dice.pop(i)
            elif isinstance(dice, YellowDice):
                # Then yellow
                return self.dice.pop(i)
            else:
                # Then red
                return self.dice.pop(i)

    def remove(self, dice: List[Dice]):
        for d in dice:
            self.dice.remove(d)

    def __iter__(self):
        return self.dice.__iter__()
