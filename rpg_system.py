from enum import Enum
import io_helper as io
import sys    # use stdin instead of input? -> so you can write diffrent things on your console

Game_State = Enum("Game_State", "STARTMENU INGAMEMENU INGAME SKILLTREE INVENTORY HISTORY")

class RPG_System(object):
    def __init__(self):
        self.state = Game_State.STARTMENU
        self.should_running = True
        self.startmenu_commands = {'new game':lambda:self.new_game()}
        self.ingamemenu_commands = dict()
        self.ingame_commands = dict()

    def run(self):
        while self.should_running:
            if self.state == Game_State.STARTMENU:
                self.run_startmenu()

    def run_startmenu(self):
        io.print_with_delay("Startmenü:\n    >> Neues Spiel <<\n    >> Lade Spiel <<\n    >> Informationen <<\n    >> Credits <<\n    >> Exit <<")
        while True:
            user_input = io.get_input()
            if user_input != None:
                # work with input
                if user_input == "neues spiel":
                    io.print_with_only_delay(f"{io.UP(7)}Startmenü:\n    {io.REVERSED}>> Neues Spiel <<{io.END}\n    >> Lade Spiel <<\n    >> Informationen <<\n    >> Credits <<\n    >> Exit <<", 0, 0)
                elif user_input == "lade spiel":
                    pass
                elif user_input == "informationen":
                    pass
                elif user_input == "credits":
                    pass
                elif user_input == "exit":
                    pass
                else: 
                    #io.print_with_only_delay(io.UP(1)+io.CLEAR_LINE(2)+io.LEFT(100))
                    io.print_with_only_delay(io.UP(1)+io.CLEAR_LINE(2)+io.SET_COLUMN(0))

                # prepare for new input
                io.print_with_only_delay(io.DOWN(1) + io.CLEAR_LINE(2) + io.LEFT(100))

    def new_game(self):
        pass

    def load_game(self):
        pass

    def save_game(self):
        pass


if __name__ == "__main__":
    RPG_System().run()
    