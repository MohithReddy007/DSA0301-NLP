import re

text = "My email is student@example.com and my phone is 9876543210."

emails = re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)
phones = re.findall(r'\b\d{10}\b', text)

print("Emails:", emails)
print("Phones:", phones)

pattern = r"\bPython\b"
match = re.search(pattern, "I am learning Python programming.")
print("Python found:", bool(match))
