import sys
from tables import copy_char, get_table, print_table, get_dict_of
from ascii_buttons import SAVED, RESETTED

QUIT = "q"
SAVE = "save"
FAVOURITES = "favs"
RESET = "reset"
TABLES_PATH = "./data/tables.csv"
FAVOURITES_PATH = "./data/favourites.csv"
CSV_DELIMITER = ","

def save(key, str_to_save):
    with open(FAVOURITES_PATH, 'a') as f:
        f.write('\n')
        f.write(f'{key},{str_to_save}')
    print(SAVED)

def reset_favs():
    with open(FAVOURITES_PATH, 'w') as f:
        f.write('keyword,saved')
    print(RESETTED)

def process_valid_command(command, tables_dict) -> dict:
    table = get_table(command, tables_dict)
    print_table(table)
    return table

def first_process_command(inp):
    param_list = inp.split()
    tables_dict = get_dict_of(TABLES_PATH)
    favourites = get_dict_of(FAVOURITES_PATH)

    if len(param_list) == 1:
        command = param_list[0]

        if command == QUIT:
            sys.exit()

        if command in favourites:
            copy_char(favourites, command)
            return

        if command in tables_dict:
            return process_valid_command(command, tables_dict)
    
        print("Not a valid command...")
         
    elif len(param_list) == 2: 
        command = param_list[0]
        keyword = param_list[1]

        if command == FAVOURITES and keyword == RESET:
            reset_favs()
            return
      
        if not command in tables_dict:
            print("\nNot a valid command...\n")
            return
        
        copy_char(get_table(command, tables_dict), keyword)

    elif len(param_list) == 3: 
        command = param_list[0]
        new_fav = param_list[1]
        keyword = param_list[2]

        if command != SAVE:
            print("\nNot a valid command...\n")
            return
        
        if keyword in favourites and new_fav == favourites[keyword]:
            print(SAVED)
            return
        
        if CSV_DELIMITER in new_fav:
            new_fav = f'"{new_fav}"'
        
        if CSV_DELIMITER in keyword:
            keyword = f'"{keyword}"'

        save(keyword, new_fav)

    else:
        print("1 or 2 parameters were expected...\n")