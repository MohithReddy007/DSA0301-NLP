from transformers import pipeline

translator = pipeline(
    "translation_en_to_fr",
    model="Helsinki-NLP/opus-mt-en-fr"
)

text = "Natural language processing is an important field of artificial intelligence."
result = translator(text, max_length=100)

print("English:", text)
print("French:", result[0]["translation_text"])
