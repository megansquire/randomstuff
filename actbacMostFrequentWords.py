#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 08:21:05 2016

@author: megan
"""

from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

fname = 'actbacFB.txt'
frequency = 50

with open(fname, 'r', encoding="utf-8") as f:
    data=f.read().replace('\n', '')

# get list of most frequent words
words = word_tokenize(data)
lowercase_words = [word.lower() for word in words
                   if word not in stopwords.words() and word.isalpha()]
word_frequencies = FreqDist(lowercase_words)
most_frequent_words = FreqDist(lowercase_words).most_common(frequency)

# print out the keywords more nicely
for pair in most_frequent_words:
    print(pair[0],":",pair[1])
    
