#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 09:24:21 2016

@author: megan
"""

from gensim import corpora
from gensim.models.ldamodel import LdaModel
from gensim.parsing.preprocessing import STOPWORDS

num_topics = 2
num_words = 4
passes = 20
filename = 'actbacFB.txt'

with open(filename, encoding='utf-8') as f:
    documents = f.readlines()

texts = [[word for word in document.lower().split()
         if word not in STOPWORDS and word.isalnum()]
         for document in documents]

dictionary = corpora.Dictionary(texts)
#print(dictionary)

corpus = [dictionary.doc2bow(text) for text in texts]

lda = LdaModel(corpus,
               id2word=dictionary,
               num_topics=num_topics,
               passes=passes)

for topic in lda.print_topics(num_words=num_words):
    termNumber = topic[0]
    print(topic[0], ':', sep='')
    listOfTerms = topic[1].split('+')
    for term in listOfTerms:
        listItems = term.split('*')
        print('  ', listItems[1], '(', listItems[0], ')', sep='')
