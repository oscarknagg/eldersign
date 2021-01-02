from typing import Optional, List

from eldersign.item import Item


class Character:
    def __init__(self,
                 health: int,
                 sanity: int,
                 membership: Optional[str] = None,
                 items: List[Item] = [],
                 trophies: list = []):
        self.health = health
        self.sanity = sanity
        assert membership in ('silver_twilight', 'sheldon_gang', None)
        self.membership = membership
        self.items = items
        self.trophies = trophies

    def __repr__(self):
        return 'Character(health={},sanity={})'.format(self.health, self.sanity)
