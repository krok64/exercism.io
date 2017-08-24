def rebase(base_from, arr, base_to):
    if base_from < 2 or base_to < 2:
        raise ValueError
    result = []
    num = 0
    for i, a in enumerate(arr[::-1]):
        if a >= base_from or a < 0:
            raise ValueError 
        num += a * (base_from ** i)
    while num > 0:
        ost = num % base_to
        num = (num - ost) / base_to
        result.append(int(ost))
    return result[::-1]

