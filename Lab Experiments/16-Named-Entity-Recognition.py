"""
Experiment 16: Named Entity Recognition
Course: Natural Language Processing

Description:
This program demonstrates named entity recognition.

Author: Student
"""

import spacy

nlp = spacy.load("en_core_web_sm")
text = "Sundar Pichai works at Google in California."
doc = nlp(text)

for ent in doc.ents:
    print(ent.text, "->", ent.label_)
