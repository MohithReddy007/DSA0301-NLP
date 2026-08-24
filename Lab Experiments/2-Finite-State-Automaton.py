"""
Experiment 2: Finite State Automaton
Course: Natural Language Processing

Description:
This program demonstrates finite state automaton.

Author: Student
"""

def accepts(text):
    state = 0
    for ch in text:
        if state == 0:
            state = 1 if ch == "a" else 0
        elif state == 1:
            state = 2 if ch == "b" else (1 if ch == "a" else 0)
        elif state == 2:
            state = 1 if ch == "a" else 0
    return state == 2

for s in ["ab", "aab", "cab", "abc", "helloab"]:
    print(s, "->", accepts(s))
