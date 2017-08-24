def binary_search(arr, num):
    l = len(arr)
    if l == 0 or (num < arr[0] or num > arr[-1]):
        raise ValueError
    low = 0
    up = l
    while 1:
        if low == up:
            if arr[low]==num:
                return low
            raise ValueError
        middle = int(low + (up - low) / 2 ) 
        if num == arr[middle]:
            return middle
        elif num > arr[middle]:
            low = middle + 1
        else:
            up = middle - 1
