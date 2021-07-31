import io_helper as io
import random
import time

class Player(object):

    SKILLS = [['Feuerball'], []]

    def __init__(self, health=10, stamina=10, magic=10, skills=[], skill_tree=[0, 0, 0, 0], skill_points=0, inventory=[], equipment=[]):
        self.health = health
        self.stamina = stamina
        self.magic = magic
        self.skills = skills
        self.skill_tree = skill_tree
        self.skill_points = skill_points
        self.inventory = inventory
        self.equipment = equipment

        self.direction = random.choice(['right', 'left', 'up', 'down'])
        self.dirs = {'up':('left', 'right', 'down'), 'down':('right', 'left', 'up'), 'right':('up', 'down', 'left'), 'left':('down', 'up', 'right')}

        self.move_commands = {'laufen':self.go, 'rechts drehen':self.rotate_right, 'links drehen':self.rotate_left, 'inventar':self.open_inventory, 
                              'angriff':self.attack, 'verteidigen':self.defend, 'ausrüstung':self.open_equipment, 'magie':self.open_magic}

    def set_maze(self, maze):
        self.maze = maze

    def turn(self):
        i = 0
        # solange bis Spieler Zug mit Bewegungskosten tätigt
        while True:
            io.print_with_only_delay(f"{io.CLEAR_SCREEN(2)}{io.SET_POSITION(0, 0)}", 0, 0)
            if i < 1:
                # Adding random extras -> ein kühler Luftzug ist zu spüren, irgendetwas ist zu hören,...
                io.print_with_delay(self.look())    # auch bei look könnte es randome xtras geben
                io.print_with_delay("-> laufen\n-> rechts drehen\n-> links drehen\n-> inventar\n-> angriff\n-> verteidigen\n-> magie")
                user_input = io.get_input("\nWas willst du tun: ")
            else:
                io.print_with_only_delay(self.look(), 0, 0)
                io.print_with_only_delay("\n-> laufen\n-> rechts drehen\n-> links drehen\n-> inventar\n-> angriff\n-> verteidigen\n-> magie", 0, 0)
                user_input = io.get_input("\n\nWas willst du tun: ")
            self.move_commands[user_input]()
            i += 1

    def look(self) -> str:
            # links davon, rechts davon, gegenüber davon
        message = ""
        result = self.maze.info_pos(self.maze.get_player_pos())
        if result[self.direction] == True:
            message += f"{io.GREEN}Vor{io.END} dir ragt eine hohe Mauer empor.\n"
        else:
            message += f"{io.GREEN}Vor{io.END} dir liegt ein schmaler Weg.\n"

        left = self.dirs[self.direction][0]
        if result[left] == True:
            message += f"{io.MAGENTA}Links{io.END} von dir ragt eine hohe Mauer empor.\n"
        else:
            message += f"{io.MAGENTA}Links{io.END} von dir liegt ein schmaler Weg.\n"

        right = self.dirs[self.direction][1]
        if result[right] == True:
            message += f"{io.BLUE}Rechts{io.END} von dir ragt eine hohe Mauer empor.\n"
        else:
            message += f"{io.BLUE}Rechts{io.END} von dir liegt ein schmaler Weg.\n"

        opposite = self.dirs[self.direction][2]
        if result[right] == True:
            message += f"{io.YELLOW}Gegenüber{io.END} von dir ragt eine hohe Mauer empor.\n"
        else:
            message += f"{io.YELLOW}Gegenüber{io.END} von dir liegt ein schmaler Weg.\n"

        return message

    def go(self):
        result = self.maze.move_player(self.direction)
        io.print_with_delay(result)
        io.confirm(message=f"(drücke {io.BACKGROUND_RED}ENTER{io.END} um Fortzufahren)", fast=True)

    def rotate_right(self):
        self.direction = self.dirs[self.direction][1]
        io.print_with_delay("Du drehst dich nach rechst.")
        io.confirm(message=f"(drücke {io.BACKGROUND_RED}ENTER{io.END} um Fortzufahren)", fast=True)

    def rotate_left(self):
        self.direction = self.dirs[self.direction][0]
        io.print_with_delay("Du drehst dich nach links.")
        io.confirm(message=f"(drücke {io.BACKGROUND_RED}ENTER{io.END} um Fortzufahren)", fast=True)

    def open_inventory(self):
        pass

    def attack(self):
        # Angriff mit der primären Waffe -> Das ist standard, weitere Angriffe sind im Inventarmenü und im magiemenü verfügbar
        pass

    def defend(self):
        # Verteidigung mit Schild oder nichts
        pass

    # gibt es Ausrüstungsabteil, oder ist das im Inventar einfach eingebaut?
    def open_equipment(self):
        pass

    def open_magic(self):
        # wie erhält man Spells? -> durch Items -> Bücher oder durch Skillsystem? -> später klären
        pass

    def level_up(self):
        pass

    def skill_tree(self):
        pass
