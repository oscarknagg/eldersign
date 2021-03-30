import multiprocessing
import traceback
import unittest
import logging
import pytest

from eldersign import cards
from eldersign import core
from eldersign import dice
from eldersign import item
from eldersign.adventure import AdventureAttempt
from eldersign.policy.clue import NaiveCluePolicy


log = logging.getLogger()
log.setLevel("DEBUG")


@pytest.mark.skip
def test_single_adventure(adventure: core.AbstractAdventure):
    board = core.Board.setup_dummy_game(adventure)
    character = board.characters[0]
    character.items.append(item.Clue())

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


class TestEveryAdventure(unittest.TestCase):
    def _test_every_card_in_expansion(self, expansion: str):
        pool = multiprocessing.Pool(multiprocessing.cpu_count())
        test_results = pool.map(test_single_adventure, list(cards.expansions[expansion].values()))
        for adventure_name, board_state, exception in test_results:
            if exception:
                log.info(adventure_name)
                log.info(exception)
                import pdb; pdb.set_trace()

        log.info("Tested {} adventures".format(len(test_results)))
        self.assertFalse(any(exception for _, _, exception in test_results))

    def test_every_card_base(self):
        self._test_every_card_in_expansion('base')

    def test_every_card_unseen_forces(self):
        self._test_every_card_in_expansion('unseen_forces')

    def test_particular_adventure(self):
        # adventure = cards.expansions['unseen_forces']['strange_robberies']
        adventure = cards.base.mysterious_tome
        adventure_name, board_state, exception = test_single_adventure(adventure)
        if exception:
            import pdb; pdb.set_trace()
