from abc import ABC, abstractmethod
from typing import List, Tuple, Optional
import logging

from eldersign.dice import Dice, DicePool
from eldersign.symbol import Symbol

log = logging.getLogger(__name__)


class Task(ABC):
    def __init__(self, symbols: List[Symbol], membership: Optional[str] = None):
        self.symbols: List[Symbol] = symbols
        assert membership in ('silver_twilight', 'sheldon_gang', None)
        self.membership = membership

        self.complete = False

    def __repr__(self):
        return 'Task({})'.format(','.join([str(sym) for sym in self.symbols]))

    def __len__(self):
        return len(self.symbols)

    def check_requirements(self, dice: List[Dice]) -> Optional[List[Tuple[Symbol, List[Dice]]]]:
        """Checks whether the requirements of this task are met.

        Returns:
            A mapping between symbols and the matched dice if the requirements are met,
            otherwise None.
        """
        used_dice = set()
        requirements_matched = []
        for task_symbol in self.symbols:
            log.debug("Checking requirements for symbol: {}".format(task_symbol))
            matching_dice_sets = task_symbol.match([d for d in dice if d not in used_dice])

            if matching_dice_sets:
                log.debug("Matched the following combinations of dice: {}".format(matching_dice_sets))

                # Take the match with the smallest number of dice
                matching_dice_sets = sorted(matching_dice_sets, key=lambda x: len(x), reverse=False)
                matched_dice = matching_dice_sets[0]
                used_dice = used_dice.union(set(matched_dice))
                requirements_matched.append((task_symbol, matched_dice))
            else:
                # One of the symbols cannot be matched
                return None

        return requirements_matched


class SuccessfulTask:
    def __init__(self, task: Task, dice: List[Dice]):
        self.task = task
        self.dice = dice

    def __repr__(self):
        return 'SuccessfulTask(task={}, dice=[{}])'.format(self.task, ','.join([str(d) for d in self.dice]))


class CluePolicy(ABC):
    @abstractmethod
    def act(self, dice: DicePool, adventure: 'AbstractAdventure'):
        raise NotImplementedError


class AbstractAdventure(ABC):
    def __init__(self, tasks: List[Task]):
        assert all(isinstance(task, Task) for task in tasks)
        self.tasks = tasks
        self.task_completion = {task: False for task in tasks}

    @property
    def incomplete_tasks(self):
        tasks = []
        for t in self.tasks:
            if not t.complete:
                tasks.append(t)

        return tasks

    @property
    @abstractmethod
    def available_tasks(self):
        raise NotImplementedError

    def __len__(self):
        return len(self.tasks)

    def __repr__(self):
        return '{}(\n\t{}\n)'.format(self.__class__.__name__, '\n\t'.join([str(task) for task in self.tasks]))

    @abstractmethod
    def check(self, dice_pool_roll: List[Dice]) -> List[SuccessfulTask]:
        """Checks if any of the task requirements are met"""
        raise NotImplementedError

    def complete_task(self, task: Task):
        task.complete = True

    @property
    def is_complete(self) -> bool:
        return all(task.complete for task in self.tasks)