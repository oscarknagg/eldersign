from typing import List, Any, Optional

from eldersign.core import Task, SuccessfulTaskOption, log, AbstractAdventure, AdventureEffect, Investigator, InvestigatorEffect
from eldersign.dice import Dice, DicePool
from eldersign.policy.clue import CluePolicy, FreezeMatchedDice
from eldersign.policy.focus import FocusPolicy, NeverFocus
from eldersign.symbol import Terror


class UnorderedAdventure(AbstractAdventure):
    def check(self, dice_pool_roll: List[Dice], character: Investigator) -> List[SuccessfulTaskOption]:
        successful_tasks = []
        for task in self.incomplete_tasks:
            log.debug("Checking requirements for {}".format(task))
            met_task_requirements = task.check_requirements(dice_pool_roll, character)
            if met_task_requirements is not None:
                dice_used = [dice for symbol, dice_group in met_task_requirements for dice in dice_group]
                successful_task = SuccessfulTaskOption(
                    task,
                    dice_used
                )
                successful_tasks.append(successful_task)

        return successful_tasks

    @property
    def available_tasks(self):
        return self.incomplete_tasks


class OrderedAdventure(AbstractAdventure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.current_task = 0

    def check(self, dice_pool_roll: List[Dice], character: Investigator) -> List[SuccessfulTaskOption]:
        task = self.tasks[self.current_task]

        # There can be multiple ways to satisfy the requirements of even
        # a single task
        met_task_requirements = task.check_requirements(dice_pool_roll, character)

        if met_task_requirements is not None:
            dice_used = [dice for symbol, dice_group in met_task_requirements for dice in dice_group]
            successful_task = SuccessfulTaskOption(
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
                 investigator: Investigator,
                 clue_policy: Optional[CluePolicy] = None,
                 focus_policy: Optional[FocusPolicy] = None):
        self.adventure = adventure
        self.dice_pool = dice_pool
        self.investigator = investigator
        self.clue_policy = clue_policy or FreezeMatchedDice(reroll_investigation_below=3)
        self.focus_policy = focus_policy or NeverFocus()

        self.force_failed = False

    def _apply_membership(self):
        for task in self.adventure.tasks:
            if self.investigator.membership and task.membership == self.investigator.membership:
                log.debug("Completing task {} due to membership".format(task))
                self.adventure.complete_task(task)

    def apply_consequences(self, succeeded: bool):
        if succeeded:
            consequences = self.adventure.rewards
            self.investigator.trophies.append(self.adventure)
        else:
            consequences = self.adventure.penalties

            # Loose blessing on failure
            if self.investigator.blessed:
                self.investigator.blessed = False

        for effect in consequences:
            if isinstance(effect, InvestigatorEffect):
                effect.apply_effect(self.investigator)
            elif isinstance(effect, AdventureEffect):
                effect.apply_effect(self, self.adventure.board)
            else:
                raise TypeError("{} of type {} is not expected.".format(effect, type(effect)))

    def finish(self, succeeded: bool):
        # Reset task status
        self.force_failed = False
        for task in self.adventure.tasks:
            task.complete = False

        if isinstance(self.adventure, OrderedAdventure):
            self.adventure.current_task = 0

        self.apply_consequences(succeeded)

    def attempt(self) -> bool:
        """True if the adventure is completed."""
        log.debug("Attempting adventure:\n{}".format(self.adventure))
        self.dice_pool.unfreeze()
        self.adventure.entry_effect(self, self.adventure.board)
        self._apply_membership()
        self.adventure.num_attempts += 1

        while len(self.dice_pool) > 0:
            self.dice_pool.roll()
            log.debug('Rolled {}'.format(','.join(str(d.symbol) for d in self.dice_pool)))

            # Check result
            successful_tasks = self.adventure.check(self.dice_pool, self.investigator)
            # What's in successful task?
            # A list of matches
            # - Each match contains a reference to the task being completed
            # - and the dice that it would take
            if successful_tasks:
                # Choose "largest" successful task
                successful_tasks = sorted(successful_tasks, key=lambda x: x.green_dice_equivalent, reverse=True)
                task_to_complete = successful_tasks[0].task
                self.adventure.complete_task(task_to_complete)
                log.debug("Requirements met, completing task {}.".format(self.adventure.tasks.index(task_to_complete)))
                # Remove dice corresponding to this task
                self.dice_pool.remove(successful_tasks[0].dice)
                self.dice_pool.unfreeze()
                for cost in task_to_complete.costs:
                    cost.apply(self.investigator)
            else:
                # Handle failures
                # Apply terror
                if Terror() in self.dice_pool:
                    self.adventure.terror_effect(self, self.adventure.board)

                # Apply clue policy
                if len(self.investigator.clues) > 0:
                    log.debug("Using a clue with {} clues remaining".format(len(self.investigator.clues)))
                    # Retry using a clue to re-roll
                    self.clue_policy.act(self.dice_pool, self.adventure)
                    self.investigator.remove_clue()
                    continue

                # Apply focus policy
                self.focus_policy.act(self.dice_pool, self.adventure)

                # Remove a die
                log.debug("Requirements not met, discarding a dice.")
                self.dice_pool.discard()

            log.debug("{} tasks and {} die remaining.".format(
                len([task for task in self.adventure.tasks if not task.complete]),
                len(self.dice_pool)
            ))

            if self.force_failed:
                self.finish(False)
                return False

            if self.adventure.is_complete:
                self.finish(True)
                return True

        self.finish(False)
        return False
