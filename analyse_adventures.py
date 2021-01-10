from copy import deepcopy
import multiprocessing
import argparse
import logging
import uuid
import json
import os

from eldersign import cards
from eldersign import core
from eldersign import dice
from eldersign.adventure import AdventureAttempt
from eldersign.policy.clue import FreezeMatchedDice


log = logging.getLogger()
log.setLevel('INFO')
handler = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s.%(module)s.%(funcName)s Line:%(lineno)d: %(asctime)s %(message)s')
handler.setFormatter(fmt=formatter)
log.addHandler(handler)


SCENARIOS = [
    {'name': 'green_locked',    'dice': {'green': 5, 'yellow': 0, 'red': 0}, 'clue': 0},
    {'name': 'default',         'dice': {'green': 6, 'yellow': 0, 'red': 0}, 'clue': 0},
    {'name': 'yellow',          'dice': {'green': 6, 'yellow': 1, 'red': 0}, 'clue': 0},
    {'name': 'red',             'dice': {'green': 6, 'yellow': 0, 'red': 1}, 'clue': 0},
    {'name': 'yellow+red',      'dice': {'green': 6, 'yellow': 1, 'red': 1}, 'clue': 0},
    {'name': 'clue',            'dice': {'green': 6, 'yellow': 0, 'red': 0}, 'clue': 1},
    {'name': 'clue*3',          'dice': {'green': 6, 'yellow': 0, 'red': 0}, 'clue': 3},
    {'name': 'yellow+red+clue', 'dice': {'green': 6, 'yellow': 0, 'red': 0}, 'clue': 3},
    {'name': 'geared',          'dice': {'green': 6, 'yellow': 1, 'red': 1}, 'clue': 3},
]


def setup_attempt(adventure: core.AbstractAdventure, scenario: dict) -> AdventureAttempt:
    copied_adventure = deepcopy(adventure)
    board = core.Board.setup_dummy_game(deepcopy(adventure))
    copied_adventure.board = board
    dice_pool = dice.DicePool.from_dice_counts(**scenario['dice'])
    adventure_attempt = AdventureAttempt(
        copied_adventure,
        dice_pool,
        board.characters[0],
        num_clues=scenario['clue'],
        clue_policy=FreezeMatchedDice(reroll_investigation_below=3),
    )

    return adventure_attempt


def run_attempt(attempt: AdventureAttempt, run_dir: str, adventure_id: str, scenario: str):
    before = attempt.adventure.board.state_dict()
    succeeded = attempt.attempt()
    after = attempt.adventure.board.state_dict()
    attempt_uuid = uuid.uuid4().hex
    with open(f'{run_dir}/{adventure_id}/{attempt_uuid}.json', 'w') as f:
        json.dump({
            'uuid': attempt_uuid,
            'scenario': scenario,
            'before': before,
            'after': after,
            'succeeded': succeeded
        }, f)


def setup_dir(run_dir: str) -> str:
    try:
        os.makedirs(run_dir)
    except FileExistsError:
        split = run_dir.split('__')
        if len(split) == 2:
            run_dir = split[0] + '__' + str(int(split[1]) + 1)
        else:
            run_dir = run_dir + '__1'
    return run_dir


def main(args: argparse.Namespace):
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    args.run_dir = setup_dir(args.run_dir)
    for expansion in args.expansions:
        for adventure_id, adventure in cards.expansions[expansion].items():
            os.makedirs(os.path.join(args.run_dir, adventure_id))

            for scenario in SCENARIOS:
                log.info("Adventure: {}, scenario = {}".format(adventure.name, scenario['name']))
                # Make N lots of this scenario
                boards = pool.starmap(setup_attempt, [(adventure, scenario)]*args.num_repeats)

                # Run all attempts
                starmap_args = (
                    boards,
                    [args.run_dir]*args.num_repeats,
                    [adventure_id]*args.num_repeats,
                    [scenario]*args.num_repeats,
                )
                starmap_args = list(zip(*starmap_args))
                pool.starmap(run_attempt, starmap_args)

        #     break
        # break

    pool.close()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--num-repeats', '-n', type=int, default=10000)
    parser.add_argument('--run-dir')
    parser.add_argument('--expansions', nargs='+', default=['base', 'unseen_forces'])
    args = parser.parse_args()

    main(args)
