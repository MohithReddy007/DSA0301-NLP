"""
Experiment 20: TF-IDF Information Retrieval
Course: Natural Language Processing

Description:
This program demonstrates tf-idf information retrieval.

Author: Student
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Python is useful for natural language processing",
    "Natural language processing uses machine learning",
    "Python is popular for data science"
]

query = ["Python natural language"]

vectorizer = TfidfVectorizer()
matrix = vectorizer.fit_transform(documents + query)

scores = cosine_similarity(matrix[-1], matrix[:-1]).flatten()

for i, score in sorted(enumerate(scores), key=lambda x: x[1], reverse=True):
    print(f"Document {i + 1}: {score:.4f}")
