import io_helper as io
import random
import time

class Player(object):

    #SKILLS = [['Feuerball'], []]

    def __init__(self, health=10, shield=5, stamina=10, magic=10, level=0, inventory=[]):
        self.health = health
        self.shield = shield
        self.stamina = stamina
        self.magic = magic
        self.inventory = inventory
        self.first_time = True

        self.direction = random.choice(['right', 'left', 'up', 'down'])
        self.dirs = {'up':('left', 'right', 'down'), 'down':('right', 'left', 'up'), 'right':('up', 'down', 'left'), 'left':('down', 'up', 'right')}

        self.move_commands = {'laufen':self.go, 'rechts drehen':self.rotate_right, 'links drehen':self.rotate_left, 'inventar':self.open_inventory, 
                               'exit':self.exit}

    def set_maze(self, maze):
        self.maze = maze

    def turn(self):
        # solange bis Spieler Zug mit Bewegungskosten tätigt
        while True:
            io.print_with_only_delay(f"{io.CLEAR_SCREEN(2)}{io.SET_POSITION(0, 0)}", 0, 0)
            self.maze.check_exit(self.direction)
            if self.first_time:
                self.first_time = False
                # Adding random extras -> ein kühler Luftzug ist zu spüren, irgendetwas ist zu hören,...
                io.print_with_delay(self.look())    # auch bei look könnte es randome xtras geben
                io.print_with_delay("-> laufen\n-> rechts drehen\n-> links drehen\n-> inventar\n-> exit")
                user_input = io.get_input("\nWas willst du tun: ")
            else:
                io.print_with_only_delay(self.look(), 0, 0)
                io.print_with_only_delay("\n-> laufen\n-> rechts drehen\n-> links drehen\n-> inventar\n-> exit", 0, 0)
                user_input = io.get_input("\n\nWas willst du tun: ")
            try:
                result = self.move_commands[user_input]()
            except KeyError:
                io.confirm("Diesen key gibt es nicht!", fast=True)
                continue
            if result == 'exit':
                return 'EXIT'
            elif result == 1:
                break

    def look(self) -> str:
            # links davon, rechts davon, gegenüber davon
        message = ""
        result = self.maze.info_pos(self.maze.get_player_pos())
        if result[self.direction] == True:
            message += f"{io.GREEN}Vor{io.END} dir ragt eine hohe Mauer empor.\n"
        else:
            if self.maze.enemy_in_front(self.direction):
                message += f"Ein Monster tut sich {io.GREEN}vor{io.END} dir auf!"
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
        if result[opposite] == True:
            message += f"{io.YELLOW}Gegenüber{io.END} von dir ragt eine hohe Mauer empor.\n"
        else:
            message += f"{io.YELLOW}Gegenüber{io.END} von dir liegt ein schmaler Weg.\n"

        return message

    def go(self):
        result = self.maze.move_player(self.direction)
        io.print_with_delay(result)
        io.confirm(message=f"(drücke {io.BACKGROUND_RED}ENTER{io.END} um Fortzufahren)", fast=True)
        return 1

    def rotate_right(self):
        self.direction = self.dirs[self.direction][1]
        io.print_with_delay("Du drehst dich nach rechst.")
        io.confirm(message=f"(drücke {io.BACKGROUND_RED}ENTER{io.END} um Fortzufahren)", fast=True)
        return 0

    def rotate_left(self):
        self.direction = self.dirs[self.direction][0]
        io.print_with_delay("Du drehst dich nach links.")
        io.confirm(message=f"(drücke {io.BACKGROUND_RED}ENTER{io.END} um Fortzufahren)", fast=True)
        return 0

    def open_inventory(self):
        while True:
            io.print_with_only_delay(f"{io.CLEAR_SCREEN(2)}{io.SET_POSITION(0,0)}Inventar:\n\n", 0, 0)
            for i, item in enumerate(self.inventory):
                io.print_with_only_delay(f"    {i}. {item.name}\n", 0, 0)
            io.print_with_only_delay(f"\n(gibt 'benutze'+*leerzeichen*+'Item-id' ein, um das Item zu verwenden.)", 0, 0)
            user_input = io.get_input("\nWas willst du tun: ")
            if user_input == 'exit' or user_input == 'weiter':
                break
            elif user_input.split(" ")[0] == 'benutze':
                try:
                    self.inventory[int(user_input.split(" ")[1])].use(self.direction)
                    return 1
                except IndexError:
                    pass
        return 0

    def damage(self, damage:int):
        damage -= self.shield
        self.shield = max(0, self.shield-damage)
        if damage > 0:
            self.health -= damage

    def add_inventory(self, item):
        self.inventory += [item]

    def level_up(self):
        pass

    def exit(self):
        pass
