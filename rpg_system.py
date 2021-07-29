from enum import Enum
import io_helper as io
import time
from player import Player
from map import Labyrinth

Game_State = Enum("Game_State", "STARTMENU INGAMEMENU INGAME SKILLTREE INVENTORY HISTORY")

# using Hashing for fast decisions -> perfom better than if-statements
class RPG_System(object):
    def __init__(self):
        self.state = Game_State.STARTMENU
        self.should_running = True
        self.startmenu_commands = {'neues spiel':self.new_game, 'lade spiel':self.load_game, 'informationen':self.get_informationen,
                                    'credits':self.credits, 'exit':self.exit}
        self.ingamemenu_commands = dict()
        self.ingame_commands = dict()

    def run(self):
        while self.should_running:
            if self.state == Game_State.STARTMENU:
                self.run_startmenu()
        exit(0)

    def run_startmenu(self):
        io.print_with_delay("Startmenü:\n    >> Neues Spiel <<\n    >> Lade Spiel <<\n    >> Informationen <<\n    >> Credits <<\n    >> Exit <<")
        while True:
            user_input = io.get_input()
            if user_input != None:
                # work with input
                try:
                    result = self.startmenu_commands[user_input]()

                    if result == "BREAK":
                        break
                except KeyError:
                    io.print_with_only_delay("Es wurde kein solches Schlüsselwort gefunden!")
                    io.get_input("")
                    io.print_with_only_delay(f"{io.UP(1)}{io.CLEAR_LINE(2)}{io.UP(1)}{io.CLEAR_LINE(2)}{io.SET_COLUMN(0)}", 0, 0)

    def new_game(self):
        io.print_with_only_delay(f"{io.UP(7)}Startmenü:\n    {io.REVERSED}>> Neues Spiel <<{io.END}\n    >> Lade Spiel <<\n    >> Informationen <<\n    >> Credits <<\n    >> Exit <<", 0, 0)
        io.print_with_only_delay(io.DOWN(1) + io.CLEAR_LINE(2) + io.LEFT(100))
        io.print_with_delay("Lade neues Spiel...")
        time.sleep(0.5)
        # init Game
        self.round = 0
        io.print_with_delay("Labyrinth wird erschaffen...")
        self.labyrinth = Labyrinth()
        io.print_with_delay("Spieler wird erstellt...")
        self.player = Player()
        self.state = Game_State.INGAME
        return "BREAK"

    def load_game(self):
        io.print_with_only_delay(f"{io.UP(7)}Startmenü:\n    >> Neues Spiel <<\n    {io.REVERSED}>> Lade Spiel <<{io.END}\n    >> Informationen <<\n    >> Credits <<\n    >> Exit <<", 0, 0)
        io.print_with_only_delay(f"{io.DOWN(1)}{io.CLEAR_LINE(2)}{io.SET_COLUMN(0)}", 0, 0)

    def get_informationen(self):
        io.print_with_only_delay(f"{io.UP(7)}Startmenü:\n    >> Neues Spiel <<\n    >> Lade Spiel <<\n    {io.REVERSED}>> Informationen <<{io.END}\n    >> Credits <<\n    >> Exit <<", 0, 0)
        io.print_with_only_delay(f"{io.DOWN(1)}{io.CLEAR_LINE(2)}{io.SET_COLUMN(0)}", 0, 0)

    def credits(self):
        io.print_with_only_delay(f"{io.UP(7)}Startmenü:\n    >> Neues Spiel <<\n    >> Lade Spiel <<\n    >> Informationen <<\n    {io.REVERSED}>> Credits <<{io.END}\n    >> Exit <<", 0, 0)
        io.print_with_only_delay(f"{io.DOWN(1)}{io.CLEAR_LINE(2)}{io.SET_COLUMN(0)}", 0, 0)

    def exit(self):
        io.print_with_only_delay(f"{io.UP(7)}Startmenü:\n    >> Neues Spiel <<\n    >> Lade Spiel <<\n    >> Informationen <<\n    >> Credits <<\n    {io.REVERSED}>> Exit <<{io.END}", 0, 0)
        io.print_with_only_delay(io.DOWN(1) + io.CLEAR_LINE(2) + io.SET_COLUMN(0))
        while True:
            result = io.get_input("Bist du dir sicher? (y/n) ")
            if result == "n":
                io.print_with_only_delay(f"{io.UP(1)}{io.CLEAR_LINE(2)}{io.SET_COLUMN(0)}{io.UP(6)}Startmenü:\n    >> Neues Spiel <<\n    >> Lade Spiel <<\n    >> Informationen <<\n    >> Credits <<\n    >> Exit <<\n", 0, 0)
                return
            elif result == "y":
                break
            else:
                io.print_char_with_only_delay(f"{io.UP(1)}{io.CLEAR_LINE(2)}{io.SET_COLUMN(0)}", 0, 0)
        io.print_with_delay("System offline...")
        time.sleep(0.5)
        self.should_running = False
        return "BREAK"

    def run_ingame(self):
        while True:
            while True:
                # Player action -> neue Runde, nur wenn wirklich eine Aktion
                pass

    def save_game(self):
        pass

    def next_round(self):
        pass

    def next_labyrinth_level(self):
        pass


if __name__ == "__main__":
    RPG_System().run()
    