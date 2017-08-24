import re
import itertools
import collections

nums = "0123456789"
result = None

def solve(phrase):
    l_side, r_side = [x.strip() for x in phrase.split("==")]
    letters = set(re.sub("[ =+]", "", phrase))
    l_side = [x.strip() for x in l_side.split("+")]
    no_zero_letters = set()
    no_zero_letters.add(r_side[0])
    for word in l_side:
        no_zero_letters.add(word[0])

    global result
    result = None

    result = for_N(0, list(letters), [-1 for x in range(len(list(letters)))], l_side, r_side, no_zero_letters)
    return result    


def for_N(ch_num, arr, l_to_n, l_side, r_side, no_zero_letters):
    global result
    if not (result is None):
        return result
    ch = arr[ch_num]
    for num in range(10):
        for i in range(ch_num+1, len(arr)):
            l_to_n[i] = -1
        if (not num in l_to_n) and (not (num == 0 and ch in no_zero_letters)):
            l_to_n[ch_num] = num
        else:
            continue
        if ch_num < len(arr) - 1:
            for_N(ch_num + 1, arr, l_to_n, l_side, r_side, no_zero_letters)
        else:
            l_sum = 0
            r_sum = 0
            for a in l_side:
                l_sum += word_to_num(a, arr, l_to_n)
            r_sum = word_to_num(r_side, arr, l_to_n)
            if l_sum == r_sum:
                result = {}
                for i, ch in enumerate(arr):
                    result[ch] = l_to_n[i]
                return result
    return result


def word_to_num(word, letters, w_to_num):
    result = 0
    w_len = len(word)
    for i in range(w_len):
        idx = letters.index(word[i])
        result += w_to_num[idx] * (10 ** (w_len - i - 1))
    return result


if __name__ == '__main__':
    print(solve("SEND + MORE == MONEY"))
