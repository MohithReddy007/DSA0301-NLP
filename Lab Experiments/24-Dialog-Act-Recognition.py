"""
Experiment 24: Dialog Act Recognition
Course: Natural Language Processing

Description:
This program demonstrates dialog act recognition.

Author: Student
"""

def dialog_act(sentence):
    s = sentence.lower().strip()

    if s.endswith("?"):
        return "QUESTION"
    if any(s.startswith(x) for x in ["hi", "hello", "hey"]):
        return "GREETING"
    if any(x in s for x in ["thank you", "thanks"]):
        return "THANKS"
    if any(x in s for x in ["please", "could you", "can you"]):
        return "REQUEST"
    if any(x in s for x in ["bye", "goodbye"]):
        return "GOODBYE"
    return "STATEMENT"

dialog = [
    "Hello!",
    "Can you help me?",
    "Please send the notes.",
    "Thank you!",
    "Goodbye!"
]

for utterance in dialog:
    print(utterance, "->", dialog_act(utterance))
