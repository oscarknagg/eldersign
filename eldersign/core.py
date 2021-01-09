from abc import ABC, abstractmethod
from typing import List, Tuple, Optional
import logging

from eldersign.dice import Dice, DicePool
from eldersign.symbol import Symbol
from eldersign.character import Character


log = logging.getLogger(__name__)


class AdventureEffect(ABC):
    @abstractmethod
    def __call__(self, adventure_atttempt, eldersign):
        raise NotImplementedError


class Cost(ABC):
    @abstractmethod
    def check(self, character: Character) -> bool:
        raise NotImplementedError

    @abstractmethod
    def apply(self, character: Character):
        raise NotImplementedError


class HealthCost(Cost):
    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return 'Health({})'.format(self.value)

    def check(self, character: Character):
        return character.health > self.value

    def apply(self, character: Character):
        log.debug("Applying {} to {}".format(self, character))
        character.health -= self.value


class SanityCost(Cost):
    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return 'Sanity({})'.format(self.value)

    def check(self, character: Character):
        return character.sanity > self.value

    def apply(self, character: Character):
        log.debug("Applying {} to {}".format(self, character))
        character.sanity -= self.value


class Task(ABC):
    def __init__(self,
                 symbols: List[Symbol],
                 costs: Optional[List[Cost]] = None,
                 membership: Optional[str] = None):
        self.symbols: List[Symbol] = symbols
        self.costs: List[Cost] = costs or []
        assert membership in ('silver_twilight', 'sheldon_gang', None)
        self.membership = membership

        self.complete = False

    def __repr__(self):
        if self.membership:
            return 'Task({})-{}'.format(','.join([str(sym) for sym in self.symbols+self.costs]), self.membership)
        else:
            return 'Task({})'.format(','.join([str(sym) for sym in self.symbols+self.costs]))

    def __len__(self):
        return len(self.symbols)

    def check_requirements(self, dice: List[Dice], character: Character) -> Optional[List[Tuple[Symbol, List[Dice]]]]:
        """Checks whether the requirements of this task are met.

        Returns:
            A mapping between symbols and the matched dice if the requirements are met,
            otherwise None.
        """
        used_dice = set()
        requirements_matched = []
        # Check dice symbols
        for task_symbol in self.symbols:
            log.debug("Checking requirements for symbol: {}".format(task_symbol))
            matching_dice_sets = task_symbol.match([d for d in dice if d not in used_dice])

            if matching_dice_sets:
                log.debug("Matched the following combinations of dice: {}".format(matching_dice_sets))

                # Take the match with the smallest number of dice
                matching_dice_sets = sorted(matching_dice_sets, key=lambda x: len(x), reverse=False)
                matched_dice = matching_dice_sets[0]
                used_dice = used_dice.union(set(matched_dice))

                costs_met = all(cost.check(character) for cost in self.costs)
                log.debug("Character costs met = {}".format(costs_met))
                if costs_met:
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
    def __init__(self,
                 tasks: List[Task],
                 trophy_value: int,
                 event: bool = False,
                 entry_effect: Optional[AdventureEffect] = None,
                 terror_effect: Optional[AdventureEffect] = None,
                 board: Optional['Board'] = None):
        assert all(isinstance(task, Task) for task in tasks)
        self.tasks = tasks
        self.trophy_value = trophy_value
        self.event = event
        self.task_completion = {task: False for task in tasks}
        self._entry_effect = entry_effect
        self._terror_effect = terror_effect
        self.board = board

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
    def check(self, dice_pool_roll: List[Dice], character: Character) -> List[SuccessfulTask]:
        """Checks if any of the task requirements are met"""
        raise NotImplementedError

    def complete_task(self, task: Task):
        task.complete = True

    @property
    def is_complete(self) -> bool:
        return all(task.complete for task in self.tasks)

    def entry_effect(self, adventure_attempt, eldersign: 'Board'):
        """Override in subclasses"""
        if self._entry_effect:
            self._entry_effect(adventure_attempt, eldersign)

    def terror_effect(self, adventure_attempt, eldersign: 'Board'):
        """Override in subclasses"""
        if self._terror_effect:
            log.debug("Triggered terror effect: {}".format(self._terror_effect.__class__.__name__))
            self._terror_effect(adventure_attempt, eldersign)


class AncientOne:
    def __init__(self, max_doom_tokens: int, max_elder_signs: int):
        self.doom_tokens = 0
        self.max_doom_tokens = max_doom_tokens
        self.elder_signs = 0
        self.max_elder_signs = max_elder_signs


class Board:
    def __init__(self,
                 adventures: List[AbstractAdventure],
                 other_worlds: List[AbstractAdventure],
                 characters: List[Character],
                 ancient_one: AncientOne):
        self.adventures = [None, ] * 6
        assert len(adventures) <= len(self.adventures)
        for i, a in enumerate(adventures):
            self.adventures[i] = a
            a.board = self

        self.other_words = [None, ] * 3
        assert len(other_worlds) <= len(self.other_words)
        for i, o in enumerate(other_worlds):
            self.other_words[i] = o

        self.characters: List[Character] = characters
        self.ancient_one = ancient_one
