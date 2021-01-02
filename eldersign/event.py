from abc import ABC, abstractmethod

event_deck = {}


class AbstractEvent(ABC):
    @abstractmethod
    def __call__(self, active_character, eldersign):
        raise NotImplementedError


