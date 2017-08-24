from collections import Counter
import math

price = {0: 0, 1: 8, 2: 7.6, 3: 7.2, 4: 6.4, 5: 6}


def calculate_total(arr):
    min_price = 1000000000
    num_books = len(arr)
    kind = Counter(arr)
    if num_books <= 1:
        return price[num_books]
    if len(kind) == 1:
        return num_books * price[1]
    for i in range(len(kind), 1, -1):
        cur_price = 0
        t_k = kind.copy()
        shelf_num = int(math.ceil(num_books / float(i)))
        shelf = [[] for x in range(shelf_num)]
        for j in range(shelf_num):
            for k, _ in t_k.most_common()[:i]:
                shelf[j].append(k)
                t_k[k] -= 1
                if t_k[k] == 0:
                    del t_k[k]
            cur_price += price[len(shelf[j])] * len(shelf[j])
        if cur_price < min_price:
            min_price = cur_price
    return min_price
