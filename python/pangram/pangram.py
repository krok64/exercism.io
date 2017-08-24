import re

def is_pangram(word):
    word = re.sub(r"[\W\d_]", "", word)
    chars = set(word.lower())
    if len(chars)==26:
    	return True
    else:
    	return False


