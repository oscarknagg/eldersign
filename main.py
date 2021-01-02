import logging
from multiprocessing import Pool
from copy import deepcopy
import numpy as np

from eldersign.adventure import AdventureAttempt
from eldersign.dice import GreenDice, DicePool, RedDice, YellowDice
from eldersign.policy.clue import FreezeMatchedDice, NaiveCluePolicy
from eldersign import cards

log = logging.getLogger()
log.setLevel('INFO')
handler = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s.%(module)s.%(funcName)s Line:%(lineno)d: %(asctime)s %(message)s')
handler.setFormatter(fmt=formatter)
log.addHandler(handler)


def attempt(adventure):
    return adventure.attempt()


def setup_attempt(adventure, green: int, yellow: int, red: int, clues: int):
    dice = []
    for _ in range(green):
        dice.append(GreenDice())
    for _ in range(yellow):
        dice.append(YellowDice())
    for _ in range(red):
        dice.append(RedDice())

    dicepool = DicePool(dice)
    adventure_attempt = AdventureAttempt(
        adventure,
        dicepool,
        num_clues=clues,
        clue_policy=NaiveCluePolicy(),
        # clue_policy=FreezeMatchedDice(reroll_investigation_below=3),
    )

    return adventure_attempt


if __name__ == '__main__':
    adventure_card = cards.founders_rock

    base = setup_attempt(adventure_card, 6, 0, 0, 0)
    red = setup_attempt(adventure_card, 6, 0, 1, 0)
    yellow = setup_attempt(adventure_card, 6, 1, 0, 0)
    clue = setup_attempt(adventure_card, 6, 0, 0, 1)
    yellow_red = setup_attempt(adventure_card, 6, 1, 1, 0)
    yellow_red_clue = setup_attempt(adventure_card, 6, 1, 1, 1)
    stacked = setup_attempt(adventure_card, 6, 1, 1, 3)

    # attempts = []
    # log.setLevel("DEBUG")
    # for i in range(1):
    #     _attempt = deepcopy(clue)
    #     _attempt.attempt()
    # exit()

    scenarios = {
        'base': base,
        'red': red,
        'yellow': yellow,
        'clue': clue,
        'yellow_red': yellow_red,
        'yellow_red_clue': yellow_red_clue,
        'stacked': stacked,

        # 'red_clue': setup_attempt(adventure_card, 6, 0, 1, 1),
        # 'stacked-yellow': setup_attempt(adventure_card, 6, 0, 1, 3),

        # 'yellow_clue': setup_attempt(adventure_card, 6, 1, 0, 1),
        # 'stacked-red': setup_attempt(adventure_card, 6, 1, 0, 3),

        # 'loadsa_clues': setup_attempt(adventure_card, 6, 0, 0, 3),
    }
    pool = Pool(4)

    for name, scenario in scenarios.items():
        attempts = []
        for i in range(10000):
            _attempt = deepcopy(scenario)
            attempts.append(_attempt)

        successes = pool.map(attempt, attempts)
        log.info("{}: {} out {} attempts successful".format(name, sum(successes), len(successes)))
