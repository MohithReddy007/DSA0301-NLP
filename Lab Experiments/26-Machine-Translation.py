from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

print("=" * 60)
print("       ENGLISH TO FRENCH MACHINE TRANSLATION")
print("=" * 60)

model_name = "Helsinki-NLP/opus-mt-en-fr"

print("\nLoading translation model...")
print("Model:", model_name)

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

print("Model loaded successfully!")

# ------------------------------------------------------------
# English sentences
# ------------------------------------------------------------

sentences = [
    "Hello, how are you?",
    "I love learning Natural Language Processing.",
    "This is a machine translation experiment.",
    "Python is easy to learn.",
    "I am studying computer science."
]
def translate_to_french(text):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        padding=True,
        truncation=True
    )

    outputs = model.generate(
        **inputs,
        max_length=100
    )

    translated_text = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return translated_text
print("\nTranslations:")
print("-" * 60)

for sentence in sentences:

    french_translation = translate_to_french(sentence)

    print("English :", sentence)
    print("French  :", french_translation)
    print("-" * 60)

print("\nTranslation completed successfully!")
