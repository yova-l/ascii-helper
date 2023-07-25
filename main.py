import sys
from asciih import show_welcome
from commands import first_process_command

# Armar un requirements...
# https://pypi.org/project/pyperclip/
# https://www.quora.com/How-can-I-install-all-the-dependencies-to-run-a-Python-script-automatically
# https://packaging.python.org/en/latest/
# https://stackoverflow.com/questions/39068700/how-do-i-create-a-console-app-in-python/39068747


def main():
    commands = sys.argv[1:]

    if len(commands) == 0:
        show_welcome()
        print("Waiting for any of the options listed above...")
    
    if len(commands) != 0:
        first_process_command(commands.join(" "))

    for line in sys.stdin: 
        first_process_command(line.rstrip())

main()

