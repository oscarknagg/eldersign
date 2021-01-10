from typing import List
from collections import deque
from abc import ABC
import random


class Item:
    def state_dict(self):
        return {
            '__class__': self.__class__.__name__
        }


class Clue(Item):
    pass


class CommonItem(Item):
    pass


class UniqueItem(Item):
    pass


class Spell(Item):
    pass


class Ally(Item):
    pass
