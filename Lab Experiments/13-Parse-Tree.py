"""
Experiment 13: CFG Parse Tree Generation
Course: Natural Language Processing

Description:
This program demonstrates cfg parse tree generation.

Author: Student
"""

import nltk
from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the'
N -> 'cat' | 'dog'
V -> 'sees'
""")

sentence = "the cat sees the dog".split()
parser = ChartParser(grammar)

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
    break
