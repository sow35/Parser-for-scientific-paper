#!/bin/sh

set -e

for pdf in ../Corpus_2021/*.pdf
do
	echo ":: Perform test on $pdf"
	python3 textract.py "$pdf"
done
