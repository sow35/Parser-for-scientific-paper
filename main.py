#!/usr/bin/python3

import sys
import subprocess
import re

MailRegex = r'[\w\.-]+@[\w\.-]+'

if len(sys.argv) < 2:
	raise ValueError("Please specify a PDF file.")

filename = sys.argv[1]
text = subprocess.check_output(['pdftotext', '-nodiag', '-nopgbrk', '-raw', filename, '-']).decode()

def getAuthors(text):
	return re.findall(MailRegex, text)

def getTitle(text):
	lines = text.split('\n')
	title = lines[0]
	i = 1
	while lines[i][0].islower():
		title += " " + lines[i]
		i += 1
	return title

def getAbstract(text):
	lines = text.split('\\n')
	i = 0
	abstract = ""
	abstractState = 0
	while i < len(lines) and abstractState < 2:
		if "ntroduction" in lines[i]:
			# print(":: Found introduction at line", i)
			break
		if abstractState == 1:
			if len(lines[i]) > 1:
				abstract += " " + lines[i]
				# print(i, lines[i])
		if "Abstract" in lines[i]:
			# print(":: Found abstract at line", i)
			abstractState = 1
		i += 1
	return abstract

authors = getAuthors(text)
title = getTitle(text)
abstract = getAbstract(text)

print(filename)
print(title)
print(" ".join(authors))
print(abstract.replace("\n", " "))
