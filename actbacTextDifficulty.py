#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 15:25:10 2016

@author: megan
"""

from textstat.textstat import textstat as ts

fname = 'actbacFB.txt'

with open(fname, 'r', encoding='utf-8') as f:
    data = f.read().replace('\n', '')


total = ts.lexicon_count(data)
difficult = ts.difficult_words(data)
fkre = ts.flesch_reading_ease(data)
grade = ts.flesch_kincaid_grade(data)
overall = ts.text_standard(data)

print("Total words:", total)
print("Difficult words:", difficult)
print("FKRE:", fkre)
print("Grade:", grade)
print("Overall readability", overall)
