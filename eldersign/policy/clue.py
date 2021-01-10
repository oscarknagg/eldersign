from abc import ABC, abstractmethod
import logging
from typing import List

from eldersign.dice import DicePool, Dice, Investigation
from eldersign.symbol import SymbolUnion
from eldersign.core import CluePolicy, AbstractAdventure

log = logging.getLogger(__name__)


class NaiveCluePolicy(CluePolicy):
    def act(self, dice: DicePool, adventure: AbstractAdventure) -> List[Dice]:
        """Re-roll all dice regardless of the situation."""
        log.debug("Using a clue to re-roll all dice.")
        return dice.dice


class FreezeMatchedDice(CluePolicy):
    def __init__(self, reroll_investigation_below: int = 1):
        self.reroll_investigation_below = reroll_investigation_below

    def act(self, dice: DicePool, adventure: AbstractAdventure):
        # Get unique task symbols
        unique_symbols = set()
        highest_investigation_count = 0
        for task in adventure.available_tasks:
            task_investigation_count = 0
            for symbol in task.symbols:
                if isinstance(symbol, SymbolUnion):
                    for sym in symbol.symbols:
                        unique_symbols.add(sym.__class__)
                else:
                    unique_symbols.add(symbol.__class__)

                if isinstance(symbol, Investigation):
                    task_investigation_count += symbol.value

            if task_investigation_count > highest_investigation_count:
                highest_investigation_count = task_investigation_count

        # Freeze dice with these symbols
        dice_frozen = []
        dice_reroll = []
        total_investigation_count_frozen = 0
        for d in dice:
            if isinstance(d.symbol, Investigation):
                matched_enough_investigations = total_investigation_count_frozen >= highest_investigation_count
                re_roll_investigation = (not matched_enough_investigations) or (d.symbol.value < self.reroll_investigation_below)
                if re_roll_investigation:
                    dice_reroll.append(d)
                else:
                    d.frozen = True
                    dice_frozen.append(d)
                    total_investigation_count_frozen += d.symbol.value
            elif d.symbol.__class__ in unique_symbols:
                d.frozen = True
                dice_frozen.append(d)
            else:
                dice_reroll.append(d)

        log.debug("Using a clue to re-roll the following dice: {}".format(dice_reroll))
        log.debug("But keeping the following frozen: {}".format(dice_frozen))
        return dice_reroll
