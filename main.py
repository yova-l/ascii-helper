import sys
import pyperclip 
# pip3 install pyperclip
# Armar un requirements...
# https://pypi.org/project/pyperclip/
# https://www.quora.com/How-can-I-install-all-the-dependencies-to-run-a-Python-script-automatically
# https://packaging.python.org/en/latest/
# https://stackoverflow.com/questions/39068700/how-do-i-create-a-console-app-in-python/39068747

def main():
    comandos = sys.argv[1:]
    print("Los comandos son: ", comandos)
  
    pyperclip.copy('Tbanana')
    res = pyperclip.paste()
    print("La pegada es: ", res)

    for comando in sys.stdin:
        res = comando.rstrip()
        print(res)

main()