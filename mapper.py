#!/usr/bin/env python
import sys
import re

stopwords = set(['the', 'and'])

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    # convert to lowercase
    # remove punctuation using regular expressions
    line = re.sub(r'[^\w\s]', '', line.strip().lower())

    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    for word in words:
	if word not in stopwords:
        	print '%s\t%s' % (word, "1")
