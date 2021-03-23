# Parser for scientific paper

The aim of this project is to create a pdf analyser for scientific papers

## This is the third "agile sprint"

In this version, the output from the second sprint is formatted in XML.
Furthermore, references are extracted from the PDF file.

For now, some errors still exist when some metadata is empty, or when parsing the references.
The program is divided in functions so that's not a big deal.
Still, some of them we'll have to fix (`getReferences` and `getAuthors`).

## Second "agile sprint"

In this version, we have the following output:

```
$ ./main.py file.pdf
file.pdf
The PDF's title
The PDF's author(s)
The abstract of the PDF
```

**Note** that some data can be missing sometimes.
This is due to some PDF not being produced by LaTeX (a workaround will be made), or wrong PDF encoding (needs investigation).

## Dependencies

`pdftotext` and Python 3 are required to run this program.

On Arch Linux, `pdftotext` can be installed with the following command: `pacman -S python-pdftotext`.
