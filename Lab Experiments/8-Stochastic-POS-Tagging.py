from collections import Counter, defaultdict

training = [
    [("I", "PRON"), ("like", "VERB"), ("Python", "NOUN")],
    [("We", "PRON"), ("use", "VERB"), ("Python", "NOUN")],
    [("Python", "NOUN"), ("is", "VERB"), ("useful", "ADJ")],
]

word_tag = defaultdict(Counter)
tag_count = Counter()

for sentence in training:
    for word, tag in sentence:
        word_tag[word.lower()][tag] += 1
        tag_count[tag] += 1

def tag_sentence(words):
    result = []
    for word in words:
        counts = word_tag[word.lower()]
        tag = counts.most_common(1)[0][0] if counts else tag_count.most_common(1)[0][0]
        result.append((word, tag))
    return result

sentence = "I like Python".split()
print(tag_sentence(sentence))
