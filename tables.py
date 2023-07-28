import pyperclip 
import csv
from ascii_buttons import COPIED

DOUBLE_QUOTES = '"'
BACK = 'back'

def get_char(table):
    if table == None:
        return
    code = input("---- Press the desired code OR 'back' to enter another command\n")
    while code != BACK:
        copy_char(table, code)
        code = input("---- Press the desired code OR 'back' to enter another command\n") 

def copy_char(table, key):
    if not key in table:
        print("Not a valid key...\n")
        return

    res = table[key]
    pyperclip.copy(res)
    print(COPIED)

def get_table(key, tables_dict) -> dict:
    table = {}
    path = tables_dict[key]
    with open(path) as f:
        reader = csv.reader(f)
        next(reader, None)
        for keyword, char in reader:
            if DOUBLE_QUOTES in char:
                char = char.strip("'")
            table[keyword] = char
    return table

def print_table(table):
    for keyword, char in table.items():
        print(f"    {keyword} = {char}")

def get_dict_of(path):
    dicc = {}
    with open(path) as f:
        reader = csv.reader(f)
        next(reader, None)
        for key, value in reader:
            dicc[key] = value
    return dicc