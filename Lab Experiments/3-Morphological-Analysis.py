"""
Experiment 3: Morphological Analysis
Course: Natural Language Processing

This program performs basic morphological analysis
without using any external Python packages.
"""

def morphological_analysis(word):

    print("\nWord:", word)

    # Prefix analysis
    prefixes = ["un", "re", "pre", "dis"]
    prefix_found = None

    for prefix in prefixes:
        if word.startswith(prefix) and len(word) > len(prefix):
            prefix_found = prefix
            break

    # Suffix analysis
    suffixes = ["ing", "ed", "ly", "ness", "er", "s"]
    suffix_found = None

    for suffix in suffixes:
        if word.endswith(suffix) and len(word) > len(suffix):
            suffix_found = suffix
            break

    # Find root word
    root = word

    if prefix_found:
        root = root[len(prefix_found):]

    if suffix_found and root.endswith(suffix_found):
        root = root[:-len(suffix_found)]

    print("Prefix :", prefix_found if prefix_found else "None")
    print("Root   :", root)
    print("Suffix :", suffix_found if suffix_found else "None")


print("=" * 50)
print("       MORPHOLOGICAL ANALYSIS")
print("=" * 50)

words = ["unhappy", "playing", "replayed", "slowly", "cats"]

for word in words:
    morphological_analysis(word)

print("\nAnalysis completed successfully.")
