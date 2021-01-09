import logging
from multiprocessing import Pool
from copy import deepcopy
import numpy as np

from eldersign.adventure import AdventureAttempt
from eldersign.dice import GreenDice, DicePool, RedDice, YellowDice
from eldersign.policy.clue import FreezeMatchedDice, NaiveCluePolicy
from eldersign import cards
from eldersign.character import Character
from eldersign.core import Board, AncientOne

log = logging.getLogger()
log.setLevel('INFO')
handler = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s.%(module)s.%(funcName)s Line:%(lineno)d: %(asctime)s %(message)s')
handler.setFormatter(fmt=formatter)
log.addHandler(handler)


def attempt(adventure):
    return adventure.attempt()


def setup_attempt(adventure,
                  green: int,
                  yellow: int,
                  red: int,
                  clues: int):
    dice = []
    for _ in range(green):
        dice.append(GreenDice())
    for _ in range(yellow):
        dice.append(YellowDice())
    for _ in range(red):
        dice.append(RedDice())

    ancient_one = AncientOne(max_doom_tokens=12, max_elder_signs=13)

    character = Character(
        health=5,
        sanity=5,
        items=[],
        trophies=[]
    )
    board = Board(
        adventures=[adventure],
        other_worlds=[],
        characters=[character],
        ancient_one=ancient_one
    )

    dicepool = DicePool(dice)
    adventure_attempt = AdventureAttempt(
        adventure,
        dicepool,
        character,
        num_clues=clues,
        # clue_policy=NaiveCluePolicy(),
        clue_policy=FreezeMatchedDice(reroll_investigation_below=3),
    )

    return adventure_attempt


if __name__ == '__main__':
    # adventure_card = cards.remains_of_the_high_priest
    #
    # attempts = []
    # log.setLevel("DEBUG")
    # for i in range(1):
    #     _attempt = setup_attempt(adventure_card, 6, 0, 0, 0)
    #     _attempt.attempt()
    #
    # log.debug(_attempt.character)
    # exit()

    for adventure_card in [cards.the_koi_pond]:
        scenarios = {
            # 'custom': setup_attempt(adventure_card, 6, 1, 1, 2),
            'base': setup_attempt(adventure_card, 6, 0, 0, 0),
            'red': setup_attempt(adventure_card, 6, 0, 1, 0),
            'yellow': setup_attempt(adventure_card, 6, 1, 0, 0),
            'clue': setup_attempt(adventure_card, 6, 0, 0, 1),
            'clues*4': setup_attempt(adventure_card, 6, 0, 0, 4),
            'yellow_red': setup_attempt(adventure_card, 6, 1, 1, 0),
            'yellow_red_clue': setup_attempt(adventure_card, 6, 1, 1, 1),
            'stacked': setup_attempt(adventure_card, 6, 1, 1, 3),
            #
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
