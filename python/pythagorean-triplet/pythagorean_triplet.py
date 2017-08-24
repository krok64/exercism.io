import math


def primitive_triplets(b):
    if b % 2 != 0:
        raise ValueError
    result = []
    for m in range(2, b):
        n = int(b / (2 * m))
        s1 = prime_factors(m)
        s2 = prime_factors(n)
        if n > 0 and not (s1 & s2) and m > n and ((m - n) % 2) == 1:
            a = int(m**2 - n**2)
            c = int(m**2 + n**2)
            if is_triplet((a, b, c)):
                if a > b:
                    result.append((b, a, c))
                else:
                    result.append((a, b, c))
    return set(result)


def triplets_in_range(n_min, n_max):
    result = []
    for a in range(n_min, n_max + 1):
        for b in range(a, n_max + 1):
            c = int(math.sqrt(a**2 + b**2))
            if c > n_max:
                break
            if is_triplet((a, b, c)):
                result.append((a, b, c))
    return set(result)


def is_triplet(nums):
    a, b, c = sorted(nums)
    if a**2 + b**2 == c**2:
        return True
    else:
        return False


def prime_factors(number):
    result = []
    i = 2
    while True:
        if number <= 1:
            break
        if number % i == 0:
            result.append(i)
            number = number / i
            i = 2
        else:
            i = i + 1

    return set(result)
