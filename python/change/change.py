import sys

INT_MAX = sys.maxsize


def find_minimum_coins(v, coins):
    if v < 0:
        return -1
    a = [0] * (v + 1)
    b = [0] * (v + 1)
    num = f_min(v, coins, a, b)
    if num == INT_MAX:
        return -1
    idx = v
    result = []
    while idx > 0:
        result.append(b[idx])
        idx = idx - b[idx]
    return result


def f_min(v, coins, knownResults, c_list):
    if v==0:
        return 0
    res = INT_MAX

    if knownResults[v] > 0:
       return knownResults[v]

    for i in [c for c in coins if c <= v]:
        sub_res = f_min(v - i, coins, knownResults, c_list)
        if sub_res != INT_MAX and sub_res + 1 < res:
            res = sub_res + 1
            knownResults[v] = res
            c_list[v] = i

    return res

