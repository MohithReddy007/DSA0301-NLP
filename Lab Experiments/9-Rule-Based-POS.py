import re

patterns = [
    (r".*ing$", "VBG"),
    (r".*ed$", "VBD"),
    (r".*ly$", "RB"),
    (r".*ness$", "NN"),
    (r".*s$", "NNS"),
]

def tag(word):
    for pattern, label in patterns:
        if re.fullmatch(pattern, word.lower()):
            return label
    return "NN"

sentence = "The students are learning quickly".split()
for word in sentence:
    print(word, "->", tag(word))
