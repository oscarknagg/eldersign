from abc import ABC, abstractmethod
from typing import List, Tuple, Optional, Any, Type, Dict, Union
from collections import deque
import logging
import random

from eldersign.dice import Dice, DicePool
from eldersign.item import Item
from eldersign.symbol import Symbol
from eldersign import item


log = logging.getLogger(__name__)


class TrophyMixin:
    def __init__(self, tropy_value: int):
        self.trophy_value = tropy_value


class DictableMixin:
    def state_dict(self):
        state_dict = {}

        for attr in dir(self):
            if isinstance(attr, DictableMixin):
                pass


class Deck:
    def __init__(self, items: list):
        deck_type = type(items[0])
        assert all(isinstance(i, deck_type) for i in items), "A deck must contain only one type."
        self.deck = deque(items)
        self.deck_type = deck_type
        self.deck_class = items[0].__class__

    def shuffle(self):
        random.shuffle(self.deck)

    def draw(self) -> Any:
        out = self.deck.pop()
        return out

    def __repr__(self):
        return 'Deck({})'.format(self.deck_class.__name__)


class AbstractEffect(ABC):
    @abstractmethod
    def apply_effect(self, *args, **kwargs):
        raise NotImplementedError

    def __call__(self, *args, **kwargs):
        if self.check_requirements(*args, **kwargs):
            self.apply_effect(*args, **kwargs)

    def check_requirements(self, *args, **kwargs) -> bool:
        """Defaults to no requirements"""
        return True


class AdventureEffect(AbstractEffect):
    @abstractmethod
    def apply_effect(self, adventure_atttempt, eldersign: 'Board'):
        raise NotImplementedError


class InvestigatorEffect(AbstractEffect):
    @abstractmethod
    def apply_effect(self, investigator: 'Investigator'):
        raise NotImplementedError


class Cost(ABC):
    @abstractmethod
    def check(self, character: 'Investigator') -> bool:
        raise NotImplementedError

    @abstractmethod
    def apply(self, character: 'Investigator'):
        raise NotImplementedError


class HealthCost(Cost):
    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return 'Health({})'.format(self.value)

    def check(self, character: 'Investigator'):
        return character.health > self.value

    def apply(self, character: 'Investigator'):
        log.debug("Applying {} to {}".format(self, character))
        character.health -= self.value


class TimeCost(Cost):
    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return 'Time({})'.format(self.value)

    def check(self, character: 'Investigator'):
        return True

    def apply(self, character: 'Investigator'):
        # TODO
        pass


class SanityCost(Cost):
    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return 'Sanity({})'.format(self.value)

    def check(self, character: 'Investigator'):
        return character.sanity > self.value

    def apply(self, character: 'Investigator'):
        log.debug("Applying {} to {}".format(self, character))
        character.sanity -= self.value


class Task(ABC):
    def __init__(self,
                 symbols: List[Symbol],
                 costs: Optional[List[Cost]] = None,
                 membership: Optional[str] = None,
                 monster_slot: Optional[int] = None):
        self._symbols: List[Symbol] = symbols
        self.costs: List[Cost] = costs or []
        assert all(isinstance(sym, Symbol) for sym in symbols)
        assert membership in ('silver_twilight', 'sheldon_gang', None)
        self.membership = membership

        self.complete = False

        # n == None means not a monster task
        # n == 0 means replacement task
        # n >= 1 or more means a partial monster task i.e. the first n symbols are
        # not convered by the monster
        if monster_slot:
            assert monster_slot < len(self)
        self.monster_slot = monster_slot

    def __repr__(self):
        if self.membership:
            return 'Task({})-{}'.format(','.join([str(sym) for sym in self.symbols+self.costs]), self.membership)
        else:
            return 'Task({})'.format(','.join([str(sym) for sym in self.symbols+self.costs]))

    def __len__(self):
        return len(self.symbols)

    @property
    def symbols(self):
        return self._symbols

    def check_requirements(self, dice: List[Dice], character: 'Investigator') -> Optional[List[Tuple[Symbol, List[Dice]]]]:
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


class EmptyMonsterTask(Task):
    def __init__(self):
        super().__init__(symbols=[], costs=[])
        self.complete = True


class RandomMonsterTask(Task):
    def __init__(self):
        # TODO: draw a random monster on init
        super().__init__(symbols=[], costs=[])
        self.complete = True


class SuccessfulTaskOption:
    def __init__(self, task: Task, dice: List[Dice]):
        self.task = task
        self.dice = dice

    def __repr__(self):
        return 'SuccessfulTask(task={}, dice=[{}])'.format(self.task, ','.join([str(d) for d in self.dice]))


class CluePolicy(ABC):
    @abstractmethod
    def act(self, dice: DicePool, adventure: 'AbstractAdventure'):
        raise NotImplementedError


class FocusPolicy(ABC):
    @abstractmethod
    def act(self, dice: DicePool, adventure: 'AbstractAdventure'):
        raise NotImplementedError


class AbstractAdventure(ABC, TrophyMixin):
    def __init__(self,
                 tasks: List[Task],
                 trophy_value: int,
                 other_world: bool = False,
                 event: bool = False,
                 entry_effect: Optional[AbstractEffect] = None,
                 terror_effect: Optional[AbstractEffect] = None,
                 at_midnight_effect: Optional[AdventureEffect] = None,
                 rewards: Optional[List[Union[AdventureEffect, InvestigatorEffect]]] = None,
                 penalties: Optional[List[Union[AdventureEffect, InvestigatorEffect]]] = None,
                 name: Optional[str] = None,
                 board: Optional['Board'] = None):
        TrophyMixin.__init__(self, tropy_value=trophy_value)
        assert all(isinstance(task, Task) for task in tasks)
        self.tasks = tasks
        self.other_world = other_world
        self.event = event
        self.task_completion = {task: False for task in tasks}
        self._entry_effect = entry_effect
        self._terror_effect = terror_effect
        self._at_midnight_effect = at_midnight_effect
        self.rewards = rewards or []
        self.penalties = penalties or []
        self.name = name

        self.board = board

        self.num_attempts = 0

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
        return '{}(\n\tname="{}"\n\ttasks=[\n\t\t{}\n\t]\n)'.format(
            self.__class__.__name__,
            self.name,
            '\n\t\t'.join([str(task) for task in self.tasks])
        )

    @abstractmethod
    def check(self, dice_pool_roll: List[Dice], character: 'Investigator') -> List[SuccessfulTaskOption]:
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
            log.debug("Triggered entry effect: {} of adventure {}".format(
                self._entry_effect.__class__.__name__, self.name))
            self._entry_effect(adventure_attempt, eldersign)

    def terror_effect(self, adventure_attempt, eldersign: 'Board'):
        """Override in subclasses"""
        if self._terror_effect:
            log.debug("Triggered terror effect: {} of adventure {}".format(
                self._terror_effect.__class__.__name__, self.name))
            
            self._terror_effect(adventure_attempt, eldersign)

    def at_midnight_effect(self, eldersign: 'Board'):
        if self._at_midnight_effect:
            log.debug("Triggered at_midnight effect: {} of adventure {}".format(
                self._at_midnight_effect.__class__.__name__, self.name))
            self._at_midnight_effect(adventure_attempt=None, eldersign=eldersign)

    def state_dict(self) -> dict:
        return {
            'name': self.name
        }

    def to_art(self):
        from tabulate import tabulate
        import numpy as np
        width = 20
        #
        # split_name = '\n'.join([self.name[i:i+width] for i in range(0, len(self.name), width)])
        #
        tasks = []
        for task in self.tasks:
            tasks.append(
                # ['[{}]'.format(sym.to_art()) for sym in task.symbols]
                ['{}'.format(sym.to_art()) for sym in task.symbols]
            )
        #
        # card_art = tabulate(tasks).split('\n')
        # print(card_art)

        tabulated = tabulate(tasks, tablefmt='grid').replace('-', '\u2500')
        print(tabulated)

        np.array([['']*15]*(len(self.tasks) + 4), dtype=np.unicode)
        np.array([['']*15]*(len(self.tasks) + 4), dtype=np.unicode)
        card_array = np.array([[' ']*15]*(len(self.tasks) + 4), dtype=np.unicode)

        card_array[0, 0] = '\u250c'
        card_array[-1, 0] = '\u2514'
        card_array[0, -1] = '\u2510'
        card_array[-1, -1] = '\u2518'
        card_array[[0, -1], 1:-1] = '\u2500'
        card_array[1:-1, [0, -1]] = '\u2502'

        for i, task in enumerate(self.tasks):
            task_chars = ''.join(['[{}]'.format(sym.to_art()) for sym in task.symbols])
            # print(task_chars)
            # import pdb; pdb.sset_trace()
            card_array[i+2, 1:1:+len(task_chars)] = np.array(task_chars, dtype=np.unicode)

        print('\n'.join(''.join(char for char in row) for row in card_array))
        # return '\n'.join(tasks)


class AncientOne:
    def __init__(self, max_doom_tokens: int, max_elder_signs: int):
        self.doom_tokens = 0
        self.max_doom_tokens = max_doom_tokens
        self.elder_signs = 0
        self.max_elder_signs = max_elder_signs

    def state_dict(self) -> dict:
        return {
            'doom_tokens': self.doom_tokens,
            'elder_signs': self.elder_signs
        }


class Clock:
    def __init__(self, board: 'Board'):
        self.day = 0
        self.hour = 0

        self.board = board

    def at_midnight(self):
        for adventure in self.board.adventures:
            adventure.at_midnight_effect(self.board)

            # TODO: Trigger monster at_midnights

    def add_hours(self, hours: int):
        self.hour += hours

        if self.hour >= 12:
            self.hour = self.hour % 12
            self.day += 1
            self.at_midnight()

        log.debug("Clock time is now {}".format(self.hour))

    def state_dict(self) -> dict:
        return {
            'hour': self.hour,
            'day': self.day
        }


class Board:
    def __init__(self,
                 adventures: List[AbstractAdventure],
                 other_worlds: List[AbstractAdventure],
                 characters: List['Investigator'],
                 ancient_one: AncientOne,
                 decks: Dict[Type, Deck]):
        self.adventures: List[Optional[AbstractAdventure]] = [None, ] * 6
        assert len(adventures) <= len(self.adventures)
        for i, a in enumerate(adventures):
            self.adventures[i] = a
            a.board = self

        self.other_words = [None, ] * 3
        assert len(other_worlds) <= len(self.other_words)
        for i, o in enumerate(other_worlds):
            self.other_words[i] = o

        self.characters: List[Investigator] = characters
        self.ancient_one = ancient_one
        self.decks = decks

        self.clock = Clock(self)

        # Just a hack for now
        self.num_monsters = 0

    @classmethod
    def setup_dummy_game(cls, adventure: AbstractAdventure) -> 'Board':
        ancient_one = AncientOne(
            max_doom_tokens=12,
            max_elder_signs=13
        )
        ancient_one.doom_tokens = 5
        ancient_one.elder_signs = 5

        characters = []
        for _ in range(3):
            character = Investigator(
                health=4,
                sanity=4,
                items=[],
                trophies=[TrophyMixin(2), TrophyMixin(1)]
            )
            characters.append(character)

        decks = {}
        for item_type in [item.CommonItem, item.UniqueItem, item.Spell, item.Ally, item.Clue]:
            items = []
            for i in range(5):
                items.append(item_type())

            decks[item_type] = Deck(items)

        board = Board(
            adventures=[adventure],
            other_worlds=[],
            characters=characters,
            ancient_one=ancient_one,
            decks=decks
        )

        return board

    def state_dict(self) -> dict:
        # TODO: Make this smart and recursive
        state_dict = {
            'adventures': [
                adventure.state_dict() for adventure in self.adventures if adventure
            ],
            'characters': [
                character.state_dict() for character in self.characters
            ],
            'ancient_one': self.ancient_one.state_dict(),
            'clock': self.clock.state_dict(),
            'num_monsters': self.num_monsters
        }

        return state_dict


class Investigator:
    def __init__(self,
                 health: int,
                 sanity: int,
                 membership: Optional[str] = None,
                 items: List[Item] = [],
                 trophies: List[TrophyMixin] = []):
        self.health = health
        self.sanity = sanity
        assert membership in ('silver_twilight', 'sheldon_gang', None)
        self.membership = membership
        self.items = items
        self.trophies = trophies

        self.cursed = False
        self.blessed = False

    def __repr__(self):
        return 'Character(health={},sanity={})'.format(self.health, self.sanity)

    def state_dict(self) -> dict:
        state_dict = {
            'health': self.health,
            'sanity': self.sanity,
            'cursed': self.cursed,
            'blessed': self.blessed,
            'items': [
                item.state_dict() for item in self.items
            ],
            'trophies': [
                trophy.trophy_value for trophy in self.trophies
            ]
        }
        return state_dict

    @property
    def clues(self) -> List[item.Clue]:
        return [i for i in self.items if isinstance(i, item.Clue)]

    def remove_clue(self):
        for i, _ in enumerate(self.items):
            if isinstance(self.items[i], item.Clue):
                self.items.pop(i)
