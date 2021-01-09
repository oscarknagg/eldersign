from typing import List
from collections import deque
from abc import ABC
import random


class Item:
    pass


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
