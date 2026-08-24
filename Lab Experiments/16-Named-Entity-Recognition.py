import spacy

nlp = spacy.load("en_core_web_sm")
text = "Sundar Pichai works at Google in California."
doc = nlp(text)

for ent in doc.ents:
    print(ent.text, "->", ent.label_)
