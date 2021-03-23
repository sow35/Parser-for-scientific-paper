#!/usr/bin/python3

import xml.etree.ElementTree as ElementTree
import subprocess
import sys

def lineToStr(line):
	lineStr = ""
	for word in line:
		lineStr += word.text + " "
	return lineStr

def blockToStr(block):
	blockStr = ""
	for line in block:
		blockStr += lineToStr(line)
	return blockStr

def getTitle(pdfXML, pdfNS):
	# if pdf was compiled from LaTeX, the title attribute is set
	# else, we'll assume it's the first block of the document
	title = pdfXML.find('./pdf:head/pdf:title', pdfNS).text
	if title is None:
		title = ""
		lines = pdfXML.findall('.//pdf:page[1]//pdf:flow[1]/pdf:block[1]/pdf:line', pdfNS)
		for line in lines:
			title += lineToStr(line)
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
	# references are found in the "References" section of the PDF
	# each reference is written in a pdf:block XML element
	# references are the last part of the pdf
	refs = []
	refsStart = pdfXML.find('.//pdf:word[.=\'References\']/../..', pdfNS)
	i = 0
	ref = pdfXML.find('.//pdf:block[last()]', pdfNS)
	print(blockToStr(ref))
	while(ref != refsStart):
		refs.append(blockToStr(ref))
		i += 1
		ref = pdfXML.find('.//pdf:block[last()-{}]'.format(i), pdfNS)
	return refs

# if len(sys.argv) < 2:
#	raise ValueError("Please specify a PDF file.")

filename = sys.argv[1]
pdfProcess = subprocess.Popen("/usr/bin/pdftotext -bbox-layout -nodiag -eol unix \'{}\' -".format(filename), stdout=subprocess.PIPE, shell=True, encoding='utf-8')

# pdfProcessOut - stdout of pdftotext's subprocess
pdfProcessOut = pdfProcess.communicate()[0]

# pdfXML - root element
pdfXML = ElementTree.fromstring(pdfProcessOut)
pdfNS = {'pdf': 'http://www.w3.org/1999/xhtml'}

title = getTitle(pdfXML, pdfNS)
authors = getAuthors(pdfXML, pdfNS)
abstract = getAbstract(pdfXML, pdfNS)
references = getReferences(pdfXML, pdfNS)

# sprint 2
# print(filename)
# print(title)
# print(authors)
# print(abstract)

# sprint 3

out_article = ElementTree.Element("article")
out_preamble = ElementTree.SubElement(out_article, "preamble")
out_preamble.text = filename
out_title = ElementTree.SubElement(out_article, "title")
out_title.text = title
out_authors = ElementTree.SubElement(out_article, "auteur")
out_authors.text = authors
out_refs = ElementTree.SubElement(out_article, "biblio")
for ref in references:
	ref_element = ElementTree.SubElement(out_refs, "reference")
	ref_element.text = ref
ElementTree.ElementTree(out_article).write("{}.xml".format(filename), xml_declaration=True, encoding="utf-8")

# we use a return code to be able to chain the program in (shell) scripts
sys.exit(0)
