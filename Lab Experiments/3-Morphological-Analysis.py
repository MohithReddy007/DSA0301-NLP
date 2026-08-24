"""
Experiment 3: Morphological Analysis using NLTK
Course: Natural Language Processing

Description:
This program demonstrates morphological analysis using nltk.

Author: Student
"""

import nltk
from nltk.stem import WordNetLemmatizer

nltk.download("wordnet", quiet=True)
nltk.download("omw-1.4", quiet=True)

lemmatizer = WordNetLemmatizer()
words = ["running", "flies", "better", "cats", "studies"]

for word in words:
    print(word, "->", lemmatizer.lemmatize(word))
