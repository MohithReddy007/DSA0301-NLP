"""
Experiment 21: Syntax-Driven Semantic Analysis
Course: Natural Language Processing

Description:
This program demonstrates syntax-driven semantic analysis.

Author: Student
"""

import nltk
from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N | 'John'
VP -> V NP
Det -> 'the'
N -> 'book'
V -> 'reads'
""")

sentence = "John reads the book".split()
parser = ChartParser(grammar)

for tree in parser.parse(sentence):
    print("Parse tree:")
    print(tree)
    print("\nNoun phrases:", [" ".join(sub.leaves()) for sub in tree.subtrees(lambda t: t.label() == "NP")])
    break
