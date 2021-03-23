#!/bin/sh

# this is a menu script to select which pdf we want to parse, as required in sprint 4
# requires zenity to be installed

zenity --file-selection --multiple --file-filter '*.pdf' --title 'Select PDF files' 2> /dev/null | tr '|' '\n' | while read file
do
	./main.py "$file"
	ret=$?
	if [ $ret -eq 0 ]
	then
		echo "Parsed $file"
	else
		echo "Errors occured when parsing $file"
	fi
done
