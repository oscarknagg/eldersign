from abc import ABC, abstractmethod
from typing import List, Tuple, Optional
import logging

from eldersign.dice import DicePool, Dice
from eldersign.symbol import Symbol


log = logging.getLogger(__name__)


class Task(ABC):
    def __init__(self, symbols: List[Symbol]):
        self.symbols: List[Symbol] = symbols
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
                # import pdb; pdb.set_trace()
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


class AbstractAdventure(ABC):
    def __init__(self, tasks: List[Task]):
        self.tasks = tasks
        self.task_completion = {task: False for task in tasks}

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


class UnorderedAdventure(AbstractAdventure):
    def __init__(self, tasks: List[Task]):
        super().__init__(tasks)

    def check(self, dice_pool_roll: List[Dice]) -> List[SuccessfulTask]:
        successful_tasks = []
        for task in self.tasks:
            met_task_requirements = task.check_requirements(dice_pool_roll)
            if met_task_requirements:
                dice_used = [dice for symbol, dice_group in met_task_requirements for dice in dice_group]
                successful_task = SuccessfulTask(
                    task,
                    dice_used
                )
                successful_tasks.append(successful_task)

        return successful_tasks


class OrderedAdventure(AbstractAdventure):
    def __init__(self, tasks: List[Task]):
        super().__init__(tasks)
        self.current_task = 0

    def check(self, dice_pool_roll: List[Dice]) -> List[SuccessfulTask]:
        task = self.tasks[self.current_task]

        # There can be multiple ways to satisfy the requirements of even
        # a single task
        met_task_requirements = task.check_requirements(dice_pool_roll)

        if met_task_requirements:
            dice_used = [dice for symbol, dice_group in met_task_requirements for dice in dice_group]
            successful_task = SuccessfulTask(
                task,
                dice_used
            )
            return [successful_task, ]
        else:
            return []

    def complete_task(self, task: Task):
        task.complete = True
        self.current_task += 1


class AdventureAttempt:
    def __init__(self, adventure: AbstractAdventure, dice_pool: DicePool):
        self.adventure = adventure
        self.dice_pool = dice_pool

    def attempt(self) -> bool:
        """True if the adventure is completed."""
        log.debug("Attempting adventure:\n{}".format(self))
        while len(self.dice_pool) > 0:
            self.dice_pool.roll()
            log.debug('Rolled {}'.format(','.join(str(d.symbol) for d in self.dice_pool)))

            # Check result
            successful_tasks = self.adventure.check(self.dice_pool)
            # What's in successful task?
            # A list of matches
            # - Each match contains a reference to the task being completed
            # - and the dice that it would take
            if successful_tasks:
                # Choose first available successful task
                self.adventure.complete_task(successful_tasks[0].task)
                log.debug("Requirements met, completing task {}.".format(self.adventure.tasks.index(successful_tasks[0].task)))
                # Remove dice corresponding to this task
                self.dice_pool.remove(successful_tasks[0].dice)
            else:
                # Remove a die
                log.debug("Requirements not met, discarding a dice.")
                self.dice_pool.discard()

            log.debug("{} tasks and {} die remaining.".format(
                len([task for task in self.adventure.tasks if not task.complete]),
                len(self.dice_pool)
            ))
            if self.adventure.is_complete:
                return True

        return False
