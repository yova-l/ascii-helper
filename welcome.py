def show_welcome():
        print("""
              
 █████╗ ███████╗ ██████╗██╗██╗      ██╗  ██╗███████╗██╗     ██████╗ ███████╗██████╗ 
██╔══██╗██╔════╝██╔════╝██║██║      ██║  ██║██╔════╝██║     ██╔══██╗██╔════╝██╔══██╗
███████║███████╗██║     ██║██║█████╗███████║█████╗  ██║     ██████╔╝█████╗  ██████╔╝
██╔══██║╚════██║██║     ██║██║╚════╝██╔══██║██╔══╝  ██║     ██╔═══╝ ██╔══╝  ██╔══██╗
██║  ██║███████║╚██████╗██║██║      ██║  ██║███████╗███████╗██║     ███████╗██║  ██║
╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝╚═╝      ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝
              
        **** Welcome! You have called the program without any parameters and 
        that's why you are seeing this. Remember that you can use the program 
        one command after another or concatenate multiple valid commands to get 
        an specific character if you remember the corresponding combination ****
              
        This program will copy to your system clipboard the character 
        you want, so you don't have to search it or enter weird combinations
        anymore.

        ------ FROM HERE YOU CAN USE THE NEXT COMMANDS: -----------------------
        |                                                                     |               
        |      * 'prog': print a list of the most frecuent characters used    |
        |        in programming i.e: $,%,!,|... .                             |
        |      * 'favs': print a list of your saved favourites.               |
        |      * 'spa': print a list of the special characters in spanish.    |
        |      * 'save <anything> <keyword>': it will save anything in your   |
        |        favourites.                                                  |
        |      * 'favs reset': it will reset your favourites.                 | 
        |                                                                     | 
        |      * 'q': quits the program.                                      |
        |      * '<keyword>': if the keyword corresponds to something you     |
        |      have saved in your favourites it will copy it.                 |
        |                                                                     |
        |                                                                     |                        
        |      ** <spa, prog, favs> can take anything as a second parameter.  |
        |      If anything corresponds to the keyword of a character it will  |
        |      copy it.                                                       |
        |                                                                     |
        -----------------------------------------------------------------------

        EXAMPLES OF USAGE: (from a terminal)
              * asciih spa A (Copied 'Á' in your clipboard)
              * asciih spa (Displays the list of 'keyword = character'
                avaliable for this command)
              * asciih prog (Displays the list of 'keyword = character' 
                avaliable for this command, i.e '1 = ~')
              * asciih prog 1 (Copied '~' in your clipboard)
        
        Hope this programs helps you, enjoy!

**************************************************************************************
""")
        
