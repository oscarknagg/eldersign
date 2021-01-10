import multiprocessing
import traceback
import unittest
import logging

from eldersign import cards
from eldersign import core
from eldersign import dice
from eldersign.adventure import AdventureAttempt
from eldersign.policy.clue import NaiveCluePolicy


log = logging.getLogger()
log.setLevel("DEBUG")


def test_single_adventure(adventure: core.AbstractAdventure):
    board = core.Board.setup_dummy_game(adventure)
    character = board.characters[0]

    def _test_single_adventure(adventure: core.AbstractAdventure):
        """Runs until success"""
        succeeded = False
        while not succeeded:
            # Reset health/stamina
            character.health = character.sanity = 5
            dice_pool = dice.DicePool.from_dice_counts(6, 1, 1)
            adventure_attempt = AdventureAttempt(
                adventure,
                dice_pool,
                character,
                num_clues=0,
                clue_policy=NaiveCluePolicy(),
            )
            succeeded = adventure_attempt.attempt()

        return adventure.name, board, None

    try:
        _test_single_adventure(adventure)
        exception_traceback = None
    except KeyboardInterrupt as e:
        raise e
    except Exception as e:
        exception_traceback = traceback.format_exc()

    return adventure.name, board, exception_traceback


class TestEveryCard(unittest.TestCase):
    def test_every_card_base(self):
        pool = multiprocessing.Pool(multiprocessing.cpu_count())
        test_results = pool.map(test_single_adventure, list(cards.expansions['base'].values())[:10])
        for adventure_name, board_state, exception in test_results:
            if exception:
                log.info(adventure_name)
                log.info(exception)
                import pdb; pdb.set_trace()

        self.assertFalse(any(exception for _, _, exception in test_results))
        import pdb; pdb.set_trace()

    def test_particular_adventure(self):
        adventure = cards.expansions['base']['a_secret_gathering']
        test_single_adventure(adventure)