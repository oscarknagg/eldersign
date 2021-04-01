from typing import List
import logging
import random

from eldersign.core import FocusPolicy, AbstractAdventure
from eldersign.dice import Dice, DicePool
from eldersign.symbol import SymbolUnion, Investigation


log = logging.getLogger(__name__)


class NeverFocus(FocusPolicy):
    def act(self, dice: DicePool, adventure: AbstractAdventure) -> List[Dice]:
        """Never use focus."""
        return []


class FreezeRandomMatchingDice(FocusPolicy):
    def __init__(self, ignore_investigation_below: int = 1):
        self.ignore_investigation_below = ignore_investigation_below

    def act(self, dice: DicePool, adventure: AbstractAdventure) -> List[Dice]:
        # Get unique task symbols
        unique_symbols = set()
        for task in adventure.available_tasks:
            for symbol in task.symbols:
                if isinstance(symbol, SymbolUnion):
                    for sym in symbol.symbols:
                        unique_symbols.add(sym.__class__)
                else:
                    unique_symbols.add(symbol.__class__)

        matching_dice = []
        for d in dice:
            if isinstance(d.symbol, Investigation):
                if d.symbol.value < self.ignore_investigation_below:
                    continue

            if d.symbol.__class__ in unique_symbols:
                matching_dice.append(d)

        if matching_dice:
            random_matching_dice = random.choice(matching_dice)
            random_matching_dice.frozen = True
            return [random_matching_dice]
        else:
            return []
