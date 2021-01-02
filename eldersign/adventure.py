from typing import List, Any, Optional

from eldersign.core import Task, SuccessfulTask, log, AbstractAdventure, AdventureEffect
from eldersign.dice import Dice, DicePool
from eldersign.policy.clue import CluePolicy, FreezeMatchedDice
from eldersign.character import Character
from eldersign.symbol import Terror


class UnorderedAdventure(AbstractAdventure):
    def __init__(self,
                 tasks: List[Task],
                 trophy_value: int,
                 event: bool = False,
                 entry_effect: Optional[AdventureEffect] = None,
                 terror_effect: Optional[AdventureEffect] = None):
        super().__init__(tasks, trophy_value, event, entry_effect=entry_effect, terror_effect=terror_effect)

    def check(self, dice_pool_roll: List[Dice], character: Character) -> List[SuccessfulTask]:
        successful_tasks = []
        for task in self.incomplete_tasks:
            log.debug("Checking requirements for {}".format(task))
            met_task_requirements = task.check_requirements(dice_pool_roll, character)
            if met_task_requirements:
                dice_used = [dice for symbol, dice_group in met_task_requirements for dice in dice_group]
                successful_task = SuccessfulTask(
                    task,
                    dice_used
                )
                successful_tasks.append(successful_task)

        return successful_tasks

    @property
    def available_tasks(self):
        return self.incomplete_tasks


class OrderedAdventure(AbstractAdventure):
    def __init__(self,
                 tasks: List[Task],
                 trophy_value: int,
                 event: bool = False,
                 entry_effect: Optional[AdventureEffect] = None,
                 terror_effect: Optional[AdventureEffect] = None):
        super().__init__(tasks, trophy_value, event, entry_effect=entry_effect, terror_effect=terror_effect)
        self.current_task = 0

    def check(self, dice_pool_roll: List[Dice], character: Character) -> List[SuccessfulTask]:
        task = self.tasks[self.current_task]

        # There can be multiple ways to satisfy the requirements of even
        # a single task
        met_task_requirements = task.check_requirements(dice_pool_roll, character)

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

    @property
    def available_tasks(self):
        return [self.tasks[self.current_task]]


class AdventureAttempt:
    def __init__(self,
                 adventure: AbstractAdventure,
                 dice_pool: DicePool,
                 character: Any,
                 num_clues: int = 0,
                 clue_policy: CluePolicy = None):
        self.adventure = adventure
        self.dice_pool = dice_pool
        self.character = character
        self.num_clues = num_clues
        self.clue_policy = clue_policy or FreezeMatchedDice()

        self.force_failed = False

    def _apply_membership(self):
        for task in self.adventure.tasks:
            if self.character.membership and task.membership == self.character.membership:
                log.debug("Completing task {} due to membership".format(task))
                self.adventure.complete_task(task)

    def attempt(self) -> bool:
        """True if the adventure is completed."""
        log.debug("Attempting adventure:\n{}".format(self.adventure))
        self.dice_pool.unfreeze()
        self.adventure.entry_effect(self, self.adventure.board)
        self._apply_membership()

        while len(self.dice_pool) > 0:
            self.dice_pool.roll()
            log.debug('Rolled {}'.format(','.join(str(d.symbol) for d in self.dice_pool)))

            # Check result
            successful_tasks = self.adventure.check(self.dice_pool, self.character)
            # What's in successful task?
            # A list of matches
            # - Each match contains a reference to the task being completed
            # - and the dice that it would take
            if successful_tasks:
                # Choose first available successful task
                task_to_complete = successful_tasks[0].task
                self.adventure.complete_task(task_to_complete)
                log.debug("Requirements met, completing task {}.".format(self.adventure.tasks.index(task_to_complete)))
                # Remove dice corresponding to this task
                self.dice_pool.remove(successful_tasks[0].dice)
                self.dice_pool.unfreeze()
                for cost in task_to_complete.costs:
                    cost.apply(self.character)
            else:
                # Handle failures

                # Apply clue policy
                if self.num_clues > 0:
                    # Retry using a clue to re-roll
                    self.clue_policy.act(self.dice_pool, self.adventure)
                    self.num_clues -= 1
                    continue

                # Apply terror
                if Terror() in self.dice_pool:
                    self.adventure.terror_effect(self, self.adventure.board)

                # Remove a die
                log.debug("Requirements not met, discarding a dice.")
                self.dice_pool.discard()

            log.debug("{} tasks and {} die remaining.".format(
                len([task for task in self.adventure.tasks if not task.complete]),
                len(self.dice_pool)
            ))

            if self.force_failed:
                return False

            if self.adventure.is_complete:
                return True

        return False
