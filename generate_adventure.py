from copy import deepcopy
import multiprocessing
import argparse
import logging

from eldersign import adventure
from eldersign import core
from eldersign import dice
from eldersign import item
from eldersign.adventure import AdventureAttempt
from eldersign.policy.clue import FreezeMatchedDice
from eldersign.policy.focus import FreezeRandomMatchingDice
from eldersign.symbol import Terror, Scroll, Skull, Investigation


log = logging.getLogger()
log.setLevel('INFO')
handler = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s.%(module)s.%(funcName)s Line:%(lineno)d: %(asctime)s %(message)s')
handler.setFormatter(fmt=formatter)
log.addHandler(handler)

SCENARIOS = [
    {'name': 'green_locked',    'dice': {'green': 5, 'yellow': 0, 'red': 0}, 'clue': 0, 'blessed': False},
    {'name': 'default',         'dice': {'green': 6, 'yellow': 0, 'red': 0}, 'clue': 0, 'blessed': False},
    {'name': 'blessed',         'dice': {'green': 6, 'yellow': 0, 'red': 0}, 'clue': 0, 'blessed': True},
    {'name': 'yellow',          'dice': {'green': 6, 'yellow': 1, 'red': 0}, 'clue': 0, 'blessed': False},
    {'name': 'red',             'dice': {'green': 6, 'yellow': 0, 'red': 1}, 'clue': 0, 'blessed': False},
    {'name': 'yellow+red',      'dice': {'green': 6, 'yellow': 1, 'red': 1}, 'clue': 0, 'blessed': False},
    {'name': 'clue',            'dice': {'green': 6, 'yellow': 0, 'red': 0}, 'clue': 1, 'blessed': False},
    {'name': 'clue*3',          'dice': {'green': 6, 'yellow': 0, 'red': 0}, 'clue': 3, 'blessed': False},
    {'name': 'yellow+red+clue', 'dice': {'green': 6, 'yellow': 1, 'red': 1}, 'clue': 1, 'blessed': False},
    {'name': 'geared',          'dice': {'green': 6, 'yellow': 1, 'red': 1}, 'clue': 3, 'blessed': False},
    {'name': 'geared+blessed',  'dice': {'green': 6, 'yellow': 1, 'red': 1}, 'clue': 3, 'blessed': True},
]
SCENARIOS = {s['name']: s for s in SCENARIOS}
ARG_TO_SYMBOL = {
    'S': Skull(),
    'L': Scroll(),  # AKA Lore
    'T': Terror()
}


def setup_attempt(adventure: core.AbstractAdventure, scenario: dict) -> AdventureAttempt:
    copied_adventure = deepcopy(adventure)
    board = core.Board.setup_dummy_game(deepcopy(adventure))
    copied_adventure.board = board
    dice_counts = scenario['dice'].copy()
    if scenario['blessed']:
        board.characters[0].blessed = True
        dice_counts['green'] += 1
    dice_pool = dice.DicePool.from_dice_counts(**dice_counts)
    for i in range(scenario['clue']):
        board.characters[0].items.append(item.Clue())
    adventure_attempt = AdventureAttempt(
        copied_adventure,
        dice_pool,
        board.characters[0],
        clue_policy=FreezeMatchedDice(reroll_investigation_below=3),
        focus_policy=FreezeRandomMatchingDice(ignore_investigation_below=3)
    )

    return adventure_attempt


def process(adventure, scenario):
    adventure_attempt = setup_attempt(adventure, SCENARIOS[scenario])
    succeeded = adventure_attempt.attempt()
    return succeeded


def parse_adventure_from_tasks(tasks, ordered) -> core.AbstractAdventure:
    if ordered:
        adventure_class = adventure.OrderedAdventure
    else:
        adventure_class = adventure.UnorderedAdventure
    generated_adventure = adventure_class(
        tasks=[
            core.Task([ARG_TO_SYMBOL.get(s) or Investigation(int(s)) for s in task.split(',')])
            for task in tasks
        ],
        trophy_value=1
    )
    log.info('\n'+str(generated_adventure))
    return generated_adventure


def main(args: argparse.Namespace):
    generated_adventure = parse_adventure_from_tasks(args.tasks, args.ordered)
    # succeeded = process(generated_adventure, args.scenario)
    # log.info(succeeded)

    starmap_args = [(generated_adventure, args.scenario),]*args.num_repeats
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    runs = pool.starmap(process, starmap_args)
    pool.close()
    log.info("Succeeded {} out of {} attempts ({:.1f}%)".format(
        sum(runs),
        len(runs),
        sum(runs)*100/len(runs)
    ))


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--tasks', nargs='+')
    parser.add_argument('--ordered', action='store_true')
    parser.add_argument('--scenario', default='default')
    parser.add_argument('--num-repeats', '-n', type=int, default=2048*4)
    args = parser.parse_args()

    main(args)
