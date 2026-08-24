import re

text = "Ravi went to the library. He borrowed a book. Ravi read it at home."

sentences = re.split(r"(?<=[.!?])\s+", text)
last_person = None
last_object = None

for sentence in sentences:
    words = sentence.split()
    for word in words:
        clean = re.sub(r"[^A-Za-z]", "", word)
        if clean in {"Ravi", "John", "Priya", "Anita"}:
            last_person = clean
        elif clean in {"book", "pen", "car"}:
            last_object = clean

    resolved = sentence.replace("He", last_person or "UNKNOWN")
    resolved = resolved.replace("he", last_person or "UNKNOWN")
    resolved = resolved.replace("it", last_object or "UNKNOWN")
    print(resolved)
