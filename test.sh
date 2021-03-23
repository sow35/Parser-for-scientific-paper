#!/bin/sh

# set -e
txt_red="$(tput setaf 1)"
txt_green="$(tput setaf 2)"
txt_bold="$(tput bold)"
txt_reset="$(tput sgr0)"

passed=0
failed=0

for pdf in ../Corpus_2021/*.pdf
do
	echo "${txt_bold}:: Perform test on $pdf ${txt_reset}"
	./main.py "$pdf"
	CODE="$?"
	if [ $CODE -eq 0 ]
	then
		echo "${txt_green}${txt_bold}:: Test on $pdf passed ${txt_reset}"
		passed=$((passed + 1))
	else
		echo "${txt_red}${txt_bold}:: Test on $pdf failed ${txt_reset}"
		failed=$((failed + 1))
	fi
	echo
done

echo "${txt_bold}${txt_green}$passed passed. ${txt_red}$failed failed. ${txt_reset}"
