def largest_product(s, num):
    s_len = len(s)
    if num > s_len or num < 0:
        raise ValueError
    max_prod=0
    for i in range(s_len-num+1):
        prod = calc_prod(s[i:i+num])
        if prod>max_prod:
            max_prod = prod
    return max_prod

def calc_prod(s):
    rez=1
    for ch in s:
        rez = rez * int(ch)
    return rez
