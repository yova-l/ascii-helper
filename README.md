must have:
	*pyhton
	*pip
	*makefile

in order: 
	*extract zip or git clone the project
	*cd theextrated
	*pip install -r requirements.txt
	*make asciiexe
	*ln -s asciiexe asciih
	*go back one folder cd ..
	*sudo mv theextracted /usr/bin
	*sudo mv asciih /usr/bin

you can call asciih now from the terminal
to unistall the program simnply:
	*sudo rm -r usr/bin/ascii-helper
	*sudo rm usr/bin/asciih
