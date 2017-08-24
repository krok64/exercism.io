import string
from collections import deque

def rotate(phrase, offset):
    if offset % len(string.ascii_lowercase) == 0:
        return phrase
    s_low = deque(string.ascii_lowercase)
    s_upp = deque(string.ascii_uppercase)
    offset = offset * (-1)
    s_low.rotate(offset)
    s_upp.rotate(offset)
    out_str=""
    for ch in phrase:
        index_low = string.ascii_lowercase.find(ch)
        index_upp = string.ascii_uppercase.find(ch)
        if index_low != -1:
            out_str = out_str + s_low[index_low]
        elif index_upp != -1:
            out_str = out_str + s_upp[index_upp]
        else:
            out_str = out_str + ch
    return out_str

