# Parser for scientific paper

The aim of this project is to create a pdf analyser for scientific papers

## This is the second "agile sprint"

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
