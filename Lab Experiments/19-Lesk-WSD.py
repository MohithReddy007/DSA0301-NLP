import nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

nltk.download("wordnet", quiet=True)
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("omw-1.4", quiet=True)

sentence = "I deposited money in the bank"
tokens = word_tokenize(sentence)

sense = lesk(tokens, "bank")
print("Sentence:", sentence)
print("Selected sense:", sense)
if sense:
    print("Definition:", sense.definition())
