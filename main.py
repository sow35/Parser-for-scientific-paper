import sys
import subprocess
import re

MailRegex = r'[\w\.-]+@[\w\.-]+'

if len(sys.argv) < 2:
	raise ValueError("Please specify a PDF file.")

filename = sys.argv[1]
text = str(subprocess.check_output(['pdftotext', '-nodiag', '-nopgbrk', filename, '-']))

def getAuthors(text):
	return re.findall(MailRegex, text.replace("\\n", "\\n "))

def getTitle(text):
	lines = text.split('\\n')
	title = lines[0][2:]
	i = 1
	while lines[i][0].islower():
		title += " " + lines[i]
		i += 1
	return title

def getAbstract(text)		# ne fonctionne pas encore
	lines = text.split('\\n')
	i = 0
	abstract = ""
	abstractState = 0
	while abstractState < 2:
		if "Abstract" in lines[i]:
			print(":: Found abstract")
			abstractState = 1
			i += 1
		if abstractState == 1:
			abstract += " " + lines[i]
			i += 1
			if "Introduction" in lines[i]:
				abstractState = 2
		else:
			i += 1
	return abstract
