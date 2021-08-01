import abc
import enemy
from enum import Enum
import io_helper as io

class Item(abc.ABC):

    Raity_Level = Enum("Raity_Level", "COMMON RARE ULTRA_RARE SECRET_RARE ENDLESS_RARE")

    def __init__(self, name:str, equipable:bool, holy:bool):
        self.name = name
        self.equipable = equipable
        self.holy = holy

    @abc.abstractmethod
    def use(self, direction):
        pass

    def set_map(self, maze):
        self.maze = maze


class Sword(Item):
    def __init__(self):
        super().__init__("Schwert", True, False) 

    def use(self, direction):
        cur_pos = self.maze.get_player_pos()
        if not self.maze.map[cur_pos].get_direction(direction):
            next_cell = self.maze.get_next_cell(cur_pos, direction)
            if type(next_cell.value) == enemy.Enemy:
                next_cell.value.get_damage(5)
                io.print_with_delay(f"{next_cell.value.name} wurde verletzt")
            else:
                io.print_with_delay(f"Du verwendest dein Schwert, aber nichts passiert.")
        else:
            io.print_with_delay("Gegen diese Mauer kann dein Schwert nichts anrichten.")


class Exit(Item):
    def __init__(self):
        super().__init__("Ausgang", True, False) 

    def use(self, direction):
        io.print_with_delay("Super. Du hast den Ausgang erreicht!")
        # print stats
        io.confirm(f"\n(Zum Beenden {io.RED}Enter{io.END} drücken)", fast=True)
        exit(0)
