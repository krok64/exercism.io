import itertools

def detect_anagrams(word, candidat_list):
    ret_list=[]
    all_words = ["".join(x) for x in itertools.permutations(word.lower())]
    if isinstance(candidat_list, str) and candidat_list.lower()!=word.lower():
        if candidat_list.lower() in all_words:
            return candidat_list
    for check_word in candidat_list:
       if check_word.lower() in all_words and check_word.lower()!=word.lower():
            ret_list.append(check_word)
    return ret_list

