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

def is_favourite(inp):
    favs = ["a","b","c","d","e","f","g","h"]
    return inp in favs

def copy_char(table, position):
    res = 'Tbanana' # En realidad aca se debe procesar obtener ese string
    pyperclip.copy(res)
    print("Copied!")

def print_list(command):
    if command == EMOJIS:
        print("1 = /...")

    elif command == PROGRAMMING:
        print("1 = /...")

    elif command == SPECIAL:
        print("1 = /...")

    elif command == QUIT:
        sys.exit()

    elif command == FAVOURITES:
        print("1 = /...")


def process_complex_command(param1, param2):
    copy_char(param1, param2)

def first_process_command(inp):
    """
    A valid [command] must have lenght one or two. In the first case a second process_command will occur,
    if the case is the other one the desired char is going to be copied, or the action will occur.
    """ 
    param_list = inp.split()

    # Wants to print an specific table or quit
    if len(param_list) == 1:
        print_list(param_list[0])

        if is_favourite(param_list[0]):
            copy_char(FAVOURITES, param_list[0])
            return
        
        return inp
         
    elif len(param_list) == 2:
        process_complex_command(param_list[0], param_list[1])
    else:
        print("1 or 2 parameters were expected...")
    

