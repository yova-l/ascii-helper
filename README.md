# ASCII-HELPER

This program will copy to your system clipboard the character you want from different pre-defined lists, so you don't have to search it or enter weird combinations anymore. In addition you can personalize your favourites commands and have anything you want to copy at a reach of a simple terminal command. 

Once installed by the instructions you can simply call 'asciih' in your terminal. In addition, can add more parameters and go directly to the list of your interest or even copy the desired character, if you recall the right combination.

## Additional parameters
* 'prog': print a list of the most frecuent characters used in programming i.e: $,%,!,|...
* 'favs': print a list of your saved favourites.
* 'spa': print a list of the special characters in spanish.
* 'save "anything" "keyword"': it will save "anything" in your favourites and "keyword" would be avaliable to be used as one of your favourites.                                                
* 'favs reset': it will reset your favourites.                                                                         
* 'q': quits the program.                                    
* '"keyword"': if the "keyword" corresponds to something you have saved in your favourites it will copy the string assigned to it.                                                                  

*'spa', 'prog' and 'favs' can take "anything" as a second parameter. If "anything" corresponds to the keyword of a character it will copy it.*                                                    

### Examples of usage (from a terminal)
* asciih spa A (Copied 'Á' in your clipboard)
* asciih spa (Displays the list of 'keyword = character' avaliable for this command)
* asciih prog (Displays the list of 'keyword = character' avaliable for this command, i.e '1 = ~', 2 = ?...)
* asciih prog 1 (Copied '~' in your clipboard)

## You must have installed:
* python3
* pip (sudo apt install -y python3-pip)
* pyperclip (pip3 install pyperclip)

## Linux Installation:
1. Download the project and extract the zip or git clone the project.
2. Open a terminal inside the parent folder of the extrated zip:
```sh
sudo mv ascii-helper /usr/bin
cd /usr/bin/ascii-helper
make asciiexe
sudo ln -s /usr/bin/ascii-helper/asciiexe /usr/bin/asciih
```
**You are ready to go! You can now call asciih now from the terminal**

3. To unistall the program simply:
```sh
sudo rm -r usr/bin/ascii-helper
sudo rm usr/bin/asciih
```
Hope this programs helps you, enjoy!