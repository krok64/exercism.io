import re

def abbreviate(phrase):
    phrase = re.sub("[^\w]", " ", phrase)
    phrase = phrase.upper().split()
    rez = ''
    for word in phrase:
        rez = rez + word[0]
    return rez
