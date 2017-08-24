import re

def is_isogram(word):
    word = re.sub(r"\W", "", word)
    chars = set(word.lower())
    if len(chars)==len(word):
    	return True
    else:
    	return False
