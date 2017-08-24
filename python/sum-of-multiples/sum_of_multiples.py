def sum_of_multiples(num, mul_list):
    rez = 0
    for i in range(num):
        for j in mul_list:
            if i % j == 0:
                rez = rez + i
                break
    return rez
