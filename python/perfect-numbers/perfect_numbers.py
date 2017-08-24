def is_perfect(num):
    return num in perf_list


perf_list = [2 ** (i - 1) * ((2 ** i) - 1) for i in range(30)]
