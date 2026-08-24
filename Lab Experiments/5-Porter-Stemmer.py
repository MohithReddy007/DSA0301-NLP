from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
words = ["playing", "played", "studies", "studying", "connected", "connection"]

for word in words:
    print(word, "->", stemmer.stem(word))
