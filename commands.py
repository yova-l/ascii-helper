import sys
import pyperclip 
# pip3 install pyperclip
"""
    pyperclip.copy('Tbanana')
    res = pyperclip.paste()
    print("La pegada es: ", res)
"""
from emojis import emojis_welcome

EMOJIS = "emo"
PROGRAMMING =   "prog"
ENGLISH = "eng"
SPECIAL = "spe"
QUIT = "q"
FAVOURITES = "fav"
SPANISH = "spa"

def copy_char(table, position):
    res = 'Tbanana' # En realidad aca se debe procesar obtener ese string
    pyperclip.copy(res)
    print("Copied!")

def process_simple_command(command):
    if command == EMOJIS:
        emojis_welcome()

    elif command == PROGRAMMING:
        emojis_welcome()

    elif command == ENGLISH:
        emojis_welcome()

    elif command == SPECIAL:
        emojis_welcome()

    elif command == QUIT:
        emojis_welcome()

    elif command == FAVOURITES:
        emojis_welcome()

    elif command == SPANISH:
        emojis_welcome()

    else:
        print("Not valid, enter a new command")
        return

    for line in sys.stdin:
        #In this case the line should be a valid code to get the char 
        copy_char(command, line.rstrip())

def process_complex_command(param1, param2):
    print("son dos")

def first_process_command(inp):
    """
    A valid [command] must have lenght one or two. In the first case a second process_command will occur,
    if the case is the other one the desired char is going to be copied, or the action will occur.
    """ 
    param_list = inp.split()
    if len(param_list) == 1:
        process_simple_command(param_list[0])

    elif len(param_list) == 2:
        process_complex_command(param_list[0], param_list[1])
    else:
        print("1 or 2 parameters were expected...")
    

