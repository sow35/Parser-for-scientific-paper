#!/usr/bin/python3

import xml.etree.ElementTree as ElementTree
import subprocess
import sys

def lineToStr(line):
	lineStr = ""
	for word in line:
		lineStr += word.text + " "
	return lineStr

def getTitle(pdfXML, pdfNS):
	# if pdf was compiled from LaTeX, the title attribute is set
	# else, we'll assume it's the first line of the document
	title = pdfXML.find('./pdf:head/pdf:title', pdfNS).text
	if title is None:
		title = lineToStr(pdfXML.find('.//pdf:line', pdfNS))
	return title

def getAuthors(pdfXML, pdfNS):
	# if pdf was compiled from LaTeX, the author metadata is filled
	author = pdfXML.find('./pdf:head/pdf:meta[@name=\'Author\']', pdfNS)
	if author is None:
		author = "Not done yet."
	else:
		author = author.attrib['content']
	return author

def getAbstract(pdfXML, pdfNS):
	# we could use full xpath, but it's not supported by ElementTree
	# abstractBlock = pdfXML.find('.//pdf:word[.=\'Abstract\']/parent::pdf:block/following-sibling::pdf:block', pdfNS)
	abstractBlock = pdfXML.find('.//pdf:word[.=\'Abstract\']/../../../pdf:block[2]', pdfNS)
	if abstractBlock is None:
		return "Could not find abstract."
	abstract = ""
	for line in abstractBlock.findall('pdf:line', pdfNS):
		abstract += lineToStr(line)
	return abstract

def getReferences(pdfXML, pdfNS):
	return "Not done yet."

# if len(sys.argv) < 2:
#	raise ValueError("Please specify a PDF file.")

filename = sys.argv[1]
pdfProcess = subprocess.Popen("/usr/bin/pdftotext -bbox-layout -nodiag -eol unix \'{}\' -".format(filename), stdout=subprocess.PIPE, shell=True)

# pdfProcessOut - stdout of pdftotext's subprocess
pdfProcessOut = pdfProcess.communicate()[0]

# pdfXML - root element
pdfXML = ElementTree.fromstring(pdfProcessOut.decode())
pdfNS = {'pdf': 'http://www.w3.org/1999/xhtml'}

title = getTitle(pdfXML, pdfNS)
authors = getAuthors(pdfXML, pdfNS)
abstract = getAbstract(pdfXML, pdfNS)

# sprint 2
print(filename)
print(title)
print(authors)
print(abstract)

# sprint 3

# out_article = ElementTree.Element("article")
# out_preamble = ElementTree.SubElement(out_article, "preamble")
# out_preamble.text = filename
# out_title = ElementTree.SubElement(out_article, "title")
# out_title.text = "test"
# ElementTree.ElementTree(out_article).write("out.xml", xml_declaration=True, encoding="utf-8")
