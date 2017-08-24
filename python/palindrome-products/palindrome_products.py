def smallest_palindrome(max_factor, min_factor=0):
    result = None
    res_prod = {}
    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            c = i * j
            a = str(c)
            b = len(a)
            is_polindome = True
            for k in range(int(b / 2)):
                if a[k] != a[b - k - 1]:
                    is_polindome = False
            if result is None and is_polindome:
                result = c
                res_prod = set((i, j))
            elif is_polindome and result > c:
                result = c
                res_prod = set((i, j))
    return ((result, res_prod))


def largest_palindrome(max_factor, min_factor=0):
    result = None
    res_prod = {}
    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            c = i * j
            a = str(c)
            b = len(a)
            is_polindome = True
            for k in range(int(b / 2)):
                if a[k] != a[b - k - 1]:
                    is_polindome = False
            if result is None and is_polindome:
                result = c
                res_prod = set((i, j))
            elif is_polindome and result < c:
                result = c
                res_prod = set((i, j))
    return ((result, res_prod))
