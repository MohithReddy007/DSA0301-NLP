import nltk
from nltk.stem import WordNetLemmatizer

nltk.download("wordnet", quiet=True)
nltk.download("omw-1.4", quiet=True)

lemmatizer = WordNetLemmatizer()
words = ["running", "flies", "better", "cats", "studies"]

for word in words:
    print(word, "->", lemmatizer.lemmatize(word))
