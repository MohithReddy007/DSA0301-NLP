def check_agreement(sentence):
    words = sentence.lower().replace(".", "").split()

    singular_subjects = {"he", "she", "it"}
    plural_subjects = {"they", "we", "students"}
    singular_verbs = {"is", "runs", "likes"}
    plural_verbs = {"are", "run", "like"}

    if len(words) < 2:
        return False

    subject, verb = words[0], words[1]

    if subject in singular_subjects and verb in singular_verbs:
        return True
    if subject in plural_subjects and verb in plural_verbs:
        return True
    return False

for s in ["He is happy", "They are happy", "He are happy"]:
    print(s, "->", check_agreement(s))
