from typing import Union, Set, List
from itertools import combinations
from abc import ABC, abstractmethod


# Fake class for type hints
class Dice:
    symbol: 'Symbol'


class Symbol(ABC):
    @abstractmethod
    def match(self, dice: List[Dice]) -> List[List[Dice]]:
        """Returns a list of all combinations of symbols that match this one."""
        raise NotImplementedError


class SymbolUnion(Symbol):
    def __init__(self, symbols: List[Symbol]):
        self.symbols = symbols

    def __repr__(self):
        return 'Union[{}]'.format(','.join([str(sym) for sym in self.symbols]))

    def match(self, dice: List[Dice]) -> List[List[Dice]]:
        matches = []
        for symbol in self.symbols:
            matches += symbol.match(dice)

        return matches


class Investigation(Symbol):
    def __init__(self, value: int):
        assert 1 <= value <= 4
        self.value = value

    def __hash__(self):
        return hash('{}({})'.format())

    def __eq__(self, other: Symbol):
        if not isinstance(other, Symbol):
            return TypeError
        else:
            return isinstance(other, Investigation) and getattr(other, 'value') == self.value

    @classmethod
    def check_comparison_types(cls, other):
        if isinstance(other, list):
            if not all(isinstance(i, Investigation) for i in other):
                raise TypeError
        else:
            if not isinstance(other, Investigation):
                raise TypeError

    def __gt__(self, other: Union['Investigation', List['Investigation']]):
        Investigation.check_comparison_types(other)
        if isinstance(other, list):
            return self.value > sum(i.value for i in other)
        else:
            return self.value > other.value

    def __lt__(self, other):
        Investigation.check_comparison_types(other)
        if isinstance(other, list):
            return self.value < sum(i.value for i in other)
        else:
            return self.value < other.value

    def __ge__(self, other):
        Investigation.check_comparison_types(other)
        if isinstance(other, list):
            return self.value >= sum(i.value for i in other)
        else:
            return self.value >= other.value

    def __le__(self, other):
        Investigation.check_comparison_types(other)
        if isinstance(other, list):
            return self.value <= sum(i.value for i in other)
        else:
            return self.value <= other.value

    def match(self, dice: List[Dice]) -> List[List[Dice]]:
        matches = []

        investigation_dice = [d for d in dice if isinstance(d.symbol, Investigation)]

        for n in range(1, len(investigation_dice)+1):
            for comb in combinations(investigation_dice, n):
                if sum(d.symbol.value for d in comb) >= self.value:
                    matches.append(list(comb))

        return matches

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.value)


class NamedSymbol(Symbol):
    def __init__(self, name: str):
        self.name = name

    def __eq__(self, other: Symbol):
        if not isinstance(other, Symbol):
            return TypeError
        else:
            return isinstance(other, NamedSymbol) and getattr(other, 'name') == self.name

    def match(self, dice: List[Dice]) -> List[List[Dice]]:
        matches = []
        for d in dice:
            if d.symbol == self:
                matches.append([d, ])

        return matches

    def __repr__(self):
        if isinstance(self, NamedSymbol) and not issubclass(self.__class__, NamedSymbol):
            return "{}('{}')".format(self.__class__.__name__, self.name)
        else:
            return self.__class__.__name__


class Terror(NamedSymbol):
    def __init__(self):
        super().__init__('terror')


class Scroll(NamedSymbol):
    def __init__(self):
        super().__init__('scroll')


class Skull(NamedSymbol):
    def __init__(self):
        super().__init__('skull')


class Wildcard(Symbol):
    def __eq__(self, other: Symbol):
        if not isinstance(other, Symbol):
            return TypeError
        else:
            return True

    def __repr__(self):
        return 'Wildcard'

    def match(self, dice: List[Dice]) -> List[List[Dice]]:
        """Matches everything"""
        return [[d, ] for d in dice]
