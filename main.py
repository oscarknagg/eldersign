import logging
from multiprocessing import Pool
from copy import deepcopy
import numpy as np

from eldersign.core import OrderedAdventure, UnorderedAdventure, Task, AdventureAttempt
from eldersign.symbol import Terror, Scroll, Skull, Investigation, SymbolUnion
from eldersign.dice import GreenDice, DicePool, RedDice, YellowDice


log = logging.getLogger()
log.setLevel('INFO')
handler = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s.%(module)s.%(funcName)s Line:%(lineno)d: %(asctime)s %(message)s')
handler.setFormatter(fmt=formatter)
log.addHandler(handler)


def attempt(adventure):
    return adventure.attempt()


if __name__ == '__main__':
    # adventure_card = OrderedAdventure(  # Unknown Kadath
    #     tasks=[
    #         Task([Terror(), SymbolUnion([Terror(), Skull()])]),
    #         Task([Terror(), Terror()]),
    #         Task([Scroll(), SymbolUnion([Terror(), Scroll()])]),
    #     ]
    # )
    # adventure_card = UnorderedAdventure(
    #     # The Dreamlands
    #     tasks=[
    #         Task([Skull(), Scroll(), Investigation(3)]),
    #     ]
    # )
    adventure_card = UnorderedAdventure(
        # City of Gugs
        tasks=[
            Task([Investigation(3), Investigation(3), Skull()]),
            Task([Skull(), Skull(), Terror()]),
        ]
    )

    dice = []
    for i in range(6):
        dice.append(GreenDice())
    dice.append(YellowDice())
    dice.append(RedDice())

    dicepool = DicePool(dice)
    adventure_attempt = AdventureAttempt(adventure_card, dicepool)

    # attempts = []
    # for i in range(1):
    #     _attempt = deepcopy(adventure_attempt)
    #     _attempt.attempt()

    attempts = []
    for i in range(10000):
        _attempt = deepcopy(adventure_attempt)
        attempts.append(_attempt)

    pool = Pool(4)
    successes = pool.map(attempt, attempts)
    log.info("{} out {} attempts successful".format(sum(successes), len(successes)))
