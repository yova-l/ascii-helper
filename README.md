# ASCII-HELPER

This program will copy to your system clipboard the character you want from different pre-defined lists so you don't have to search for it or enter weird keyboard combinations anymore. In addition, you can personalize your favourites commands and have whatever you want to copy at a reach of a simple terminal command. 

Once installed by the instructions, you can simply call 'asciih' in your terminal. You can also add more parameters to the 'asciih' call and go directly to the list of your interest or even copy the desired character, if you recall the right combination.

## Additional parameters
* 'prog': prints a list of the most frecuent characters used in programming i.e: $,%,!,|...
* 'favs': prints a list of your saved favourites.
* 'spa': prints a list of the special characters in spanish.
* 'save "anything" "keyword"': it will save "anything" in your favourites and "keyword" would be avaliable to be used as one of your favourites.                                                
* 'favs reset': it will reset your favourites.                                                                         
* 'q': quits the program.                                    
* '"keyword"': if the "keyword" corresponds to something you have saved in your favourites it will copy the string assigned to it.                                                                  

*'spa', 'prog' and 'favs' can take "anything" as a second parameter. If "anything" corresponds to the keyword of a character it will copy it.*                                                    

### Examples of usage (from a terminal)
* asciih spa A (Copied 'Á' in your clipboard)
* asciih spa (Displays a list of 'keyword = character' avaliables for this command)
* asciih prog (Displays a list of 'keyword = character' avaliables for this command, i.e '1 = ~', 2 = ?,...)
* asciih prog 1 (Copied '~' in your clipboard)

## You must have installed:
* python3
* pip (sudo apt install -y python3-pip)
* pyperclip (pip install pyperclip)

## Linux Installation:
1. Download the project and extract the zip or git clone the project.
2. Open a terminal in the parent folder of the extracted zip:
```sh
sudo mv ascii-helper /usr/bin
cd /usr/bin/ascii-helper
make asciiexe
sudo ln -s /usr/bin/ascii-helper/asciiexe /usr/bin/asciih
```
**You are ready to go! You can now call asciih from the terminal**

3.  If you get an error from the pyperclip module that looks like this:
```py
#...
    raise PyperclipException(EXCEPT_MSG)
pyperclip.PyperclipException: 
    Pyperclip could not find a copy/paste mechanism for your system.
    For more information, please visit https://pyperclip.readthedocs.io/en/latest/index.html#not-implemented-error
```
Running `sudo apt-get install xsel` in your terminal may be the solution. If it's not follow the link provided by the error.

4. To unistall the program simply:
```sh
sudo rm -r usr/bin/ascii-helper
sudo rm usr/bin/asciih
```
Hope this programs helps you, enjoy!