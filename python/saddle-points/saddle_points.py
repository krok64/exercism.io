def saddle_points(arr):
    if arr==[]:
        return set()
    cols = len(arr[0])
    rows = len(arr)
    result = []
    for i in range(rows):
        if len(arr[i]) != cols:
            raise ValueError
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == max(arr[i]):
                found = True
                for k in range(rows):
                    if arr[i][j] > arr[k][j]:
                        found = False
                        break
                if found:
                    result.append((i, j))
    return set(result)
