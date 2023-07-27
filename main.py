import sys
from asciih import show_welcome
from commands import first_process_command, copy_char

BACK = 'back'

# Armar un requirements...
# https://pypi.org/project/pyperclip/
# https://www.quora.com/How-can-I-install-all-the-dependencies-to-run-a-Python-script-automatically
# https://packaging.python.org/en/latest/
# https://stackoverflow.com/questions/39068700/how-do-i-create-a-console-app-in-python/39068747

def get_char(table):
    """PRE: the table exits, the users wants a char"""
    if table == None:
        return
    code = input("Press the desired code OR 'back' to enter another command\n")
    while code != BACK:
        copy_char(table, code)
        code = input("Press the desired code OR 'back' to enter another command\n") 

def main():
    commands = sys.argv[1:]

    if len(commands) == 0:
        show_welcome()
        print("Waiting for any of the options listed above...")
    
    if len(commands) != 0:
        table = first_process_command(" ".join(commands))
        get_char(table)

    print("\nPlease enter a valid command...\n")
    for line in sys.stdin: 
        table = first_process_command(line.rstrip())
        get_char(table)
        print("Please enter a valid command...")

main()

