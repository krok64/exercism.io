import re

orig = "abcdefghijklmnopqrstuvwxyz"
modif = "zyxwvutsrqponmlkjihgfedcba"

def encode(phrase):
    rez = ''
    phrase = re.sub("[\W_]", "", phrase.lower())
    i = 0
    for ch in phrase:
        if i==5:
            rez = rez + ' '
            i = 0
        idx = orig.find(ch)
        if idx != -1:
            rez = rez + modif[idx]
        else:
            rez = rez + ch
        i = i + 1
    return rez


def decode(phrase):
    rez=''
    phrase = re.sub("[\W]", "", phrase)
    for ch in phrase:
        idx = orig.find(ch)
        if idx != -1:
            rez = rez + modif[idx]
        else:
            rez = rez + ch
    return rez

