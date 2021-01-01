from abc import ABC, abstractmethod
import logging
from typing import List

from eldersign.dice import DicePool, Dice
from eldersign.symbol import SymbolUnion
from eldersign.core import CluePolicy, AbstractAdventure

log = logging.getLogger(__name__)


class NaiveCluePolicy(CluePolicy):
    def act(self, dice: DicePool, adventure: AbstractAdventure) -> List[Dice]:
        """Re-roll all dice regardless of the situation."""
        log.debug("Freezing no dice.")
        return dice.dice


class FreezeMatchedDice(CluePolicy):
    def act(self, dice: DicePool, adventure: AbstractAdventure):
        # Get unique task symbols
        unique_symbols = set()
        for task in adventure.incomplete_tasks:
            for symbol in task.symbols:
                if isinstance(symbol, SymbolUnion):
                    for sym in symbol.symbols:
                        unique_symbols.add(sym.__class__)
                else:
                    unique_symbols.add(symbol.__class__)

        # Freeze dice with these symbols
        dice_frozen = []
        dice_reroll = []
        for d in dice:
            if d.symbol.__class__ in unique_symbols:
                d.frozen = True
                dice_frozen.append(d)
            else:
                dice_reroll.append(d)

        log.debug("Using a clue to re-roll the following dice: {}".format(dice_reroll))
        log.debug("But keeping the following frozen: {}".format(dice_frozen))
        return dice_reroll
