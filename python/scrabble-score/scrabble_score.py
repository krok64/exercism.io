def score(word):
    worth = {1: "AEIOULNRST", 2: "DG", 3: "BCMP", 4: "FHVWY",
        5: "K", 8: "JX", 10: "QZ"}
    result = 0
    for ch in word.upper():
        result = result + get_worth(ch, worth)
    return result


def get_worth(ch, worth):
    for idx in worth:
        if ch in worth[idx]:
            return idx

