from collections import defaultdict
import random

text = "I like natural language processing. I like Python programming. Python is useful for NLP."
tokens = text.lower().replace(".", "").split()

bigrams = defaultdict(list)
for a, b in zip(tokens, tokens[1:]):
    bigrams[a].append(b)

word = "i"
result = [word]

for _ in range(12):
    if word not in bigrams:
        break
    word = random.choice(bigrams[word])
    result.append(word)

print("Generated text:")
print(" ".join(result))
