"""
Experiment 10: Transformation-Based Tagging
Course: Natural Language Processing

Description:
This program demonstrates transformation-based tagging.

Author: Student
"""

words = ["I", "book", "a", "book"]

tags = ["NN"] * len(words)

# Initial rule: pronoun
if words[0].lower() == "i":
    tags[0] = "PRP"

# Transformation rule: "book" after "I" is a verb
for i in range(1, len(words)):
    if words[i].lower() == "book" and words[i - 1].lower() == "i":
        tags[i] = "VB"

print(list(zip(words, tags)))
