import string
import re
import random
import itertools
from collections import deque

class Cipher(object):
    def __init__(self, key=None):
        if key==None:
            key=""
            for i in range(random.randint(100, 200)):
                key = key + random.choice(string.ascii_lowercase)
        if re.search("\d", key) or re.search("[A-Z]", key):
            raise ValueError
        self.key = key

    def decode(self, phrase):
        table = itertools.cycle(self.key)
        phrase = phrase.lower()
        phrase = re.sub("[^a-z]", "", phrase)
        out_str=""
        for ch in phrase:
            idx = int(ord(table.next()) - ord('a'))
            ch = ord(ch) - idx
            if ch < ord('a'):
                ch = ch + 26
            out_str = out_str + chr(ch)
        return out_str

    def encode(self, phrase):
        table = itertools.cycle(self.key)
        phrase = phrase.lower()
        phrase = re.sub("[^a-z]", "", phrase)
        out_str=""
        for ch in phrase:
            idx = ord(table.next()) - ord('a')
            ch = ord(ch) + idx
            if ch > ord('z'):
                ch = ch - 26
            out_str = out_str + chr(ch)
        return out_str


class Caesar(Cipher):
    def __init__(self):
        super(Caesar, self).__init__("d")

