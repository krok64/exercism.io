def translate(phrase):
    result = []
    for i in phrase.split():
        result.append(to_pig(i))
    return " ".join(result)


def to_pig(word):
    vowels = "aeiouy"
    consolants = "qwrtpsdfghjklzxcvbnm"
    cons_vow = ["qu", "squ"]

    if word[0] == "x":
        if word[1] not in vowels:
            return word+"ay"

    if word[0] == "y":
        if word[1] in vowels:
            return word[1:] + word[:1] + "ay"

    if word[0] in vowels:
        return word+"ay"
    else:
        for i in cons_vow:
            if word.startswith(i):
                a = len(i)
                return word[a:] + word[:a] + "ay"

        for i in range(len(word)):
            if not word[i] in consolants:
                break
        return word[i:] + word[:i] + "ay"

