#!/usr/bin/python3
import sys
from welcome import show_welcome
from commands import first_process_command
from tables import get_char

def main():
    commands = sys.argv[1:]

    if len(commands) == 0:
        show_welcome()
        print("Waiting for any of the options listed above...")
    
    if len(commands) != 0:
        table = first_process_command(" ".join(commands))
        if len(commands) > 1:
            sys.exit()
        get_char(table)

    print("Please enter a valid command...")
    for line in sys.stdin: 
        table = first_process_command(line.rstrip())
        get_char(table)
        print("Please enter a valid command...")

main()

