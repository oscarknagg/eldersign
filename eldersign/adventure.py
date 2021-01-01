from typing import List

from eldersign.core import Task, SuccessfulTask, log, AbstractAdventure
from eldersign.dice import Dice, DicePool
from eldersign.policy.clue import CluePolicy, FreezeMatchedDice


class UnorderedAdventure(AbstractAdventure):
    def __init__(self, tasks: List[Task]):
        super().__init__(tasks)

    def check(self, dice_pool_roll: List[Dice]) -> List[SuccessfulTask]:
        successful_tasks = []
        for task in self.incomplete_tasks:
            log.debug("Checking requirements for {}".format(task))
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
    def __init__(self,
                 adventure: AbstractAdventure,
                 dice_pool: DicePool,
                 num_clues: int = 0,
                 clue_policy: CluePolicy = None):
        self.adventure = adventure
        self.dice_pool = dice_pool
        self.num_clues = num_clues
        self.clue_policy = clue_policy or FreezeMatchedDice()

    def attempt(self) -> bool:
        """True if the adventure is completed."""
        log.debug("Attempting adventure:\n{}".format(self.adventure))
        self.dice_pool.unfreeze()

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
                self.dice_pool.unfreeze()
            else:
                # Handle failures

                if self.num_clues > 0:
                    # Retry using a clue to re-roll
                    self.clue_policy.act(self.dice_pool, self.adventure)
                    self.num_clues -= 1
                    continue

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
