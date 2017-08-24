def nth_prime(num):
    if num < 1:
        raise ValueError
    return p_list[num - 1]


def sieve(num):
    is_prime = [True for x in range(num + 1)]
    primes = []
    for x in range(2, num + 1):
        if is_prime[x]:
            primes.append(x)
            for i in range(x * 2, num + 1, x):
                is_prime[i] = False
    return primes


p_list = sieve(10000000)