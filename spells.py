from enum import Enum
import abc

class Spell(abc.ABC):

    Spell_Type = Enum("Spell_Type", "FIRE WATER LIGHT DARK")    # What types there are?

    def __init__(self, name:str, type, costs:int):
        self.name = name
        self.type = type
        self.costs = costs

    @abc.abstractmethod
    def use(self):
        pass
