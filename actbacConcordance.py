#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 12:37:33 2016

@author: megan
"""
import nltk
import sys
fname = 'actbacFB.txt'
outfile = 'actbacConcordanceStand.txt'
interestingWord = 'stand'
numLines = 300
width = 100

text = ''

with open(fname, 'r', encoding="utf-8") as f:
    data = f.read().replace('\n', '')

tokens = nltk.word_tokenize(data)
text = nltk.Text(tokens)

saveout = sys.stdout
SavedConcordance = open(outfile, 'w', encoding='utf-8')
sys.stdout = SavedConcordance
text.concordance(interestingWord, width=width, lines=numLines)
sys.stdout = saveout
SavedConcordance.close()

print("Succesfuly saved to outfile\n")
