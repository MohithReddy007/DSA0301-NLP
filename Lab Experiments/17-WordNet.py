"""
Experiment 17: WordNet Synset Analysis
Course: Natural Language Processing

Description:
This program demonstrates wordnet synset analysis.

Author: Student
"""

import nltk
from nltk.corpus import wordnet as wn

nltk.download("wordnet", quiet=True)
nltk.download("omw-1.4", quiet=True)

word = "bank"
synsets = wn.synsets(word)

for syn in synsets[:5]:
    print("Synset:", syn.name())
    print("Definition:", syn.definition())
    print("Examples:", syn.examples())
    print()
