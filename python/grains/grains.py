def on_square(num):
    if num<=0 or num>64:
        raise ValueError
    return 2**(num-1)

def total_after(num):
    if num<=0 or num>64:
        raise ValueError
    return sum([on_square(x) for x in range(1, num+1)])
