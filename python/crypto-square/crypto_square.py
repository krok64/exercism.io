import re
import math


def encode(phrase):
    phrase = phrase.lower()
    phrase = re.sub("[^a-z0-9]", "", phrase)
    phrase_len = len(phrase)
    if phrase_len == 0:
        return ""
    cols = int(math.ceil(math.sqrt(phrase_len)))
    rows = int(math.ceil(phrase_len / cols))
    result = []
    for i in range(cols):
        result.append(phrase[i::cols])
    return " ".join(result)
