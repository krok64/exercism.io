def prime_factors(number):
    result = []
    i = 2
    while True:
        if number == 1:
            break
        if number % i == 0:
            result.append(i)
            number = number / i
            i = 2
        else:
            i = i + 1

    return result





