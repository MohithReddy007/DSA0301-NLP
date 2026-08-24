"""
Experiment 23: Text Coherence Evaluation
Course: Natural Language Processing

Description:
This program demonstrates text coherence evaluation.

Author: Student
"""

import re
from collections import Counter

def coherence_score(text):
    sentences = [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]
    if len(sentences) < 2:
        return 1.0

    sets = []
    for sentence in sentences:
        words = set(re.findall(r"\b[a-zA-Z]+\b", sentence.lower()))
        sets.append(words)

    overlaps = []
    for a, b in zip(sets, sets[1:]):
        union = a | b
        overlaps.append(len(a & b) / len(union) if union else 0)

    return sum(overlaps) / len(overlaps)

text = "Python is a programming language. Python is widely used in NLP. NLP processes human language."
print("Coherence score:", round(coherence_score(text), 3))
