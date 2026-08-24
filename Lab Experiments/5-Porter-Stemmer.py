"""
Experiment 5: Porter Stemmer
Course: Natural Language Processing

Description:
This program demonstrates porter stemmer.

Author: Student
"""

from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
words = ["playing", "played", "studies", "studying", "connected", "connection"]

for word in words:
    print(word, "->", stemmer.stem(word))
