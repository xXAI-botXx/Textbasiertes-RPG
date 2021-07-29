import abc
from enum import Enum

class Item(abc.ABC):

    Raity_Level = Enum("Raity_Level", "COMMON RARE ULTRA_RARE SECRET_RARE ENDLESS_RARE")

    def __init__(self, name:str, equipable:bool, holy:bool, rarity_level):
        self.name = name
        self.equipable = equipable
        self.holy = holy
        self.rarity_level = rarity_level

    @abc.abstractmethod
    def use(self):
        pass
