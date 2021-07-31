import sys
import os
import time
import random
import winsound
import msvcrt

#XXX ANSI Escape Codes: XXX
# Using ANSI Escape Codes and you need os.system("color") for windows

# could save in dict
# \033 und \u001b sollten das selbe sein
# Colors
PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
MAGENTA = '\u001b[35m'
RED = '\033[91m'
WHITE = '\u001b[37m'
BLACK = '\u001b[30m'

# Background-Colors
BACKGROUND_BLACK = "\u001b[40m"
BACKGROUND_RED = "\u001b[41m"
BACKGROUND_GREEN = "\u001b[42m"
BACKGROUND_YELLOW = "\u001b[43m"
BACKGROUND_BLUE = "\u001b[44m"
BACKGROUND_MAGENTA = "\u001b[45m"
BACKGROUND_CYAN = "\u001b[46m"
BACKGROUND_WHITE = "\u001b[47m"

# Styles
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
REVERSED = "\u001b[7m"
HEADER = "\033[95m"

# Cursor Navigations -> functions!
# move cursor in A/B/C/D Direction by n characters
UP = lambda n: f"\u001b[{n}A"
DOWN = lambda n: f"\u001b[{n}B"
RIGHT = lambda n: f"\u001b[{n}C"
LEFT = lambda n: f"\u001b[{n}D"

NEXT_LINE = lambda n: f"\u001b[{n}E" #moves cursor to beginning of line n lines down
PREV_LINE = lambda n: f"\u001b[{n}F" #moves cursor to beginning of line n lines down

SET_COLUMN = lambda n: f"\u001b[{n}G" #moves cursor to column n
SET_POSITION = lambda n, m: f"\u001b[{n};{m}H" #moves cursor to row n column m


# Clearing
CLEAR_SCREEN = lambda n: f"\u001b[{n}J" #clears the screen
#    n=0 clears from cursor until end of screen,
#    n=1 clears from cursor to beginning of screen
#    n=2 clears entire screen
CLEAR_LINE = lambda n: f"\u001b[{n}K" #clears the current line
#    n=0 clears from cursor to end of line
#    n=1 clears from cursor to start of line
#    n=2 clears entire line

# Reset
END = '\033[0m'

sounds = ("DATA/typing_1.wav", "DATA/typing_3.wav", "DATA/typing_4.wav", "DATA/typing_5.wav", "DATA/typing_7.wav", "DATA/typing_8.wav", "DATA/typing_9.wav"
            , "DATA/typing_15.wav", "DATA/typing_16.wav")

# Output
print_time = 0.1
print_time_max = 4   
print_time_min = 0

def print_with_delay(txt:str, *features) -> None:
    """Print something with delay on console"""
    if len(features) > 0:
        txt = add_special_effect(txt, features)
    os.system("color")

    for c in txt:
        sys.stdout.write(c)
        sys.stdout.flush()    # forces buffer to flush the txt (normally it collect all and take it out togheter)
        if print_time_max > 0:
            if c == "\n":
                winsound.PlaySound(sounds[0], winsound.SND_ASYNC)
            else:
                winsound.PlaySound(sounds[random.randint(1, 8)], winsound.SND_ASYNC)
        #time.sleep(print_time)
        rnd = random.randint(print_time_min, print_time_max)
        time.sleep(rnd/10)
    if print_time_max <= 0:
        winsound.PlaySound(sounds[random.randint(0, 8)], winsound.SND_ASYNC)
    sys.stdout.write("\n"+END)
    sys.stdout.flush()

def print_with_only_delay(txt:str, min=print_time_min, max=print_time_max) -> None:
    """Print something with delay on console"""
    os.system("color")

    for c in txt:
        sys.stdout.write(c)
        sys.stdout.flush()    # forces buffer to flush the txt (normally it collect all and take it out togheter)
        if max > 0:
            if c == "\n":
                winsound.PlaySound(sounds[0], winsound.SND_ASYNC)
            else:
                winsound.PlaySound(sounds[random.randint(1, 8)], winsound.SND_ASYNC)
        #time.sleep(print_time)
        rnd = random.randint(min, max)
        time.sleep(rnd/10)
    #if max <= 0:
    #    winsound.PlaySound(sounds[random.randint(0, 8)], winsound.SND_ASYNC)

def print_char_with_only_delay(c:str, min=print_time_min, max=print_time_max) -> None:
    """Print something with delay on console"""
    os.system("color")

    sys.stdout.write(c)
    sys.stdout.flush()    # forces buffer to flush the txt (normally it collect all and take it out togheter)
    if max > 0:
        if c == "\n":
                winsound.PlaySound(sounds[0], winsound.SND_ASYNC)
        else:
            winsound.PlaySound(sounds[random.randint(1, 8)], winsound.SND_ASYNC)
    
def special_print(txt:str, *features) -> None:
    new_txt = txt
    for i in features:
        new_txt = i + new_txt + END
    print_with_delay(new_txt)

def print_bold(txt:str, *features) -> None:
    if len(features) != 0:
        new_txt = txt
        for i in features:
            new_txt = i + new_txt + END

        print_with_delay(BOLD+new_txt+END)
    else:
        print_with_delay(BOLD+txt+END)

def add_special_effect(txt:str, *features) -> str:    # You can add Special Effects by yourself or with this method
    if type(features[0]) == tuple:
        features = features[0]
    new_txt = txt
    for i in features:
        new_txt = i + new_txt + END
    return new_txt

# Input
def get_input(message="User: ") -> str:
    user_input = ""
    print_with_only_delay(message)
    while True:
        #user_input = sys.stdin.read(1)
        #user_input = str(msvcrt.getch(), 'utf-8')
        try:
            char = msvcrt.getch().decode()
            user_input += char
        except UnicodeDecodeError:
            return None
        #except KeyError:
        #    return None
        
        if char == "\n" or char == "\r":
            print_char_with_only_delay("\n", 0, 0)
            break
        print_char_with_only_delay(HEADER+char+END)
    return user_input.lower().replace("\r", "")

def confirm(message="", cleanup=False, fast=False):
    if fast:
        print_with_only_delay(message, 0, 0)
    else:
        print_with_only_delay(message)
    get_input("")
    if cleanup:
        print_with_only_delay(f"{CLEAR_SCREEN(2)}{SET_POSITION(0,0)}", 0, 0)

def all_unicodes():
    for i in range(0,1100):
        print(i, chr(i))

# Examples and more
def colors():
    for i in range(0, 16):
        for j in range(0, 16):
            code = str(i * 16 + j)
            sys.stdout.write(f"\u001b[38;5;{code}m{code.ljust(4)}")
        print(u"\u001b[0m")

def get_color_code(number:int):
    codes = []
    for i in range(0, 16):
        for j in range(0, 16):
            code = str(i * 16 + j)
            codes += [f"\u001b[38;5;{code}m"]
    return codes[number]

def background_colors():
    for i in range(0, 16):
        for j in range(0, 16):
            code = str(i * 16 + j)
            sys.stdout.write(f"\u001b[48;5;{code}m{code.ljust(4)}")
        print(u"\u001b[0m")

def get_background_color_code(number:int):
    codes = []
    for i in range(0, 16):
        for j in range(0, 16):
            code = str(i * 16 + j)
            codes += [f"\u001b[48;5;{code}m"]
    return codes[number]

# Cursor Usage
def loading_example():
    for p in range(101):
        sys.stdout.write(f"{LEFT(3)}{p}%")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\n")
    sys.stdout.flush()

def menu_example():
    print_with_only_delay(f"Menu:\n    -> New Game\n    -> Load Game\n    -> Exit\n")
    while True:
        user_input = input("User: ").lower()
        if user_input == "exit":
            print_with_only_delay(f"{UP(4)}    -> New Game\n    -> Load Game\n    {REVERSED}-> Exit{END}\n", 0, 0)
            print_with_only_delay(LEFT(100) + " "*6+" "*len(user_input) + LEFT(100), 0, 0)
            time.sleep(1)
            print_with_only_delay("bye...")
            print_with_only_delay(DOWN(1)+LEFT(10), 0, 0)
            time.sleep(0.5)
            break
        elif user_input == "new game":
            print_with_only_delay(f"{UP(4)}    {REVERSED}-> New Game{END}\n    -> Load Game{DOWN(2)}{LEFT(100)}", 0, 0)
            print_with_only_delay(" "*6+" "*len(user_input)+LEFT(100), 0, 0)
        elif user_input == "load game":
            print_with_only_delay(f"{UP(4)}    -> New Game\n    {REVERSED}-> Load Game{END}{DOWN(2)}{LEFT(100)}", 0, 0)
            print_with_only_delay(" "*6+" "*len(user_input)+LEFT(100), 0, 0)
        else:
            print_with_only_delay(UP(1)+" "*6+" "*len(user_input)+LEFT(100), 0, 0)


if __name__ == "__main__":
    testing = False
    if testing == True:
        print_with_delay("moin")
        print_with_delay(f"moin {add_special_effect('red_bold', RED, BOLD)}")
        print_with_delay(f"moin {add_special_effect('red', RED)}")
        print_with_delay(f"{add_special_effect('reversed', REVERSED)}")
        print_with_delay("header", HEADER)
        print_with_delay("BACKGROUND_MAGENTA", BACKGROUND_MAGENTA)
    #menu_example()
