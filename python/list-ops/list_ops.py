def map_clone(f, arr):
    return [f(x) for x in arr]


def length(arr):
    result = 0
    for a in arr:
        result += 1
    return result


def filter_clone(f, arr):
    return [x for x in arr if f(x)]


def reverse(arr):
    return arr[::-1]


def append(arr, item):
    l = length(arr)
    newlist = [""] * (l + 1)
    for i in range(l):
        newlist[i] = arr[i]
    newlist[l] = item
    return newlist

def concat(arr, arr2):
    if arr2:
        for i in arr2:
            arr = append(arr, i)
    return arr


def flat(arr):
    ret_list = []
    if arr==None:
        return None
    if (not isinstance(arr, list)) and (not isinstance(arr, tuple)):
        ret_list = []
        ret_list.append(arr)
        return ret_list
    for elem in arr:
        if elem==None or elem==[] or elem==():
            continue
        if not isinstance(elem, list):
            ret_list.append(elem)
            continue
        a=flat(elem)
        if a!=None:
            ret_list.extend(flat(elem))
    return ret_list


def foldl(f, arr, num):
    result = num
    for i in range(length(arr)):
        result = f(result, arr[i])
    return result


def foldr(f, arr, num):
    result = num
    for i in range(length(arr) - 1, -1, -1):
        result = f(arr[i], result)
    return result

