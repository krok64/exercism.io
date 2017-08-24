def sieve(num):
    is_prime = [True for x in range(num+1)]
    primes=[]
    for x in range(2, num+1):
        if is_prime[x]:
            primes.append(x)
            for i in range(x*2, num+1, x):
                is_prime[i] = False
    return primes


