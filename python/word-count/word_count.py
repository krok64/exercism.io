import re

def word_count(words):
    ret_dict={}
    words = re.sub(r'[\W_]', ' ', words)
    for word in words.lower().split():
        if word in ret_dict:
            ret_dict[word] += 1
        else:
            ret_dict[word] = 1
    return ret_dict

