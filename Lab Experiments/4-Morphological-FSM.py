"""
Experiment 4: Finite-State Morphological Parser
Course: Natural Language Processing

Description:
This program demonstrates finite-state morphological parser.

Author: Student
"""

def plural(noun):
    if noun.endswith(("s", "x", "z", "ch", "sh")):
        return noun + "es"
    if noun.endswith("y") and len(noun) > 1 and noun[-2] not in "aeiou":
        return noun[:-1] + "ies"
    return noun + "s"

for word in ["cat", "bus", "box", "baby", "dish"]:
    print(word, "->", plural(word))
