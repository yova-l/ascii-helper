import sys
import pyperclip 
import csv
# pip3 install pyperclip
"""
    pyperclip.copy('Tbanana')
    res = pyperclip.paste()
    print("La pegada es: ", res)

    emojis;emo
    programming;prog
    special;spe
    favourites;fav
    spanish;spa

"""
QUIT = "q"
DOUBLE_QUOTES = '"'

def is_favourite(inp):
    favs = ["a","b","c","d","e","f","g","h"]
    return inp in favs

def copy_char(table, key):
    if not key in table:
        print("Not a valid key...")
        return

    res = table[key]
    pyperclip.copy(res)
    print("Copied!")

def process_valid_command(command, commands_dict) -> dict:
    if command == QUIT:
        sys.exit()
    table = get_table(command, commands_dict)
    print_table(table)
    return table

def get_table(key, command_dict) -> dict:
    table = {}
    path = command_dict[key]
    with open(path) as f:
        for keyword, char in csv.reader(f,delimiter='0'):
            if DOUBLE_QUOTES in char: # RARISIMA ATAJADA MEJORAR
                char = char.strip("'")
            table[keyword] = char
    return table

def print_table(table):
    for keyword, char in table.items():
        print(f"    {keyword} = {char}")

def process_complex_command(param1, param2):
    copy_char(param1, param2)

def get_dict_of_commands(path):
    commands = {}
    with open(path) as f:
        for path_name, command in csv.reader(f):
            commands[command] = path_name
    return commands

def first_process_command(inp):
    """
    A valid [command] must have lenght one or two. In the first case a second process_command will occur,
    if the case is the other one the desired char is going to be copied, or the action will occur.
    """ 
    param_list = inp.split()
    commands_dict = get_dict_of_commands("commands.csv")

    # Wants to print an specific table or quit
    if len(param_list) == 1:
        command = param_list[0]

        #pendiente
        if is_favourite(command):
            copy_char({}, command)
            return

        if command in commands_dict:
            return process_valid_command(command, commands_dict)
    
        print("\nNot a valid command...")
         
    elif len(param_list) == 2: #pendiente
        process_complex_command(param_list[0], param_list[1])

    else:
        print("1 or 2 parameters were expected...")
    

