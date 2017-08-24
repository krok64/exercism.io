def count(arr):
    result = 0
    rows = len(arr)
    if rows==0:
        return 0
    cols = len(arr[0])
    for i in range(rows - 1):
        for j in range(cols - 1):
            if arr[i][j] == "+":
                for j2 in range(j + 1, cols):
                    if arr[i][j2]=="-":
                        continue
                    elif arr[i][j2]=="+":
                        for i2 in range(i + 1, rows):
                            if arr[i2][j2]=="|":
                                continue
                            elif arr[i2][j2]=="+": 
                                if arr[i2][j]=="+":
                                    bad_track = False
                                    for k in range(i+1, i2):
                                        if arr[k][j]!='|' and arr[k][j]!='+':
                                            bad_track = True
                                    for l in range(j+1, j2):
                                        if arr[i][l]!='-' and arr[i][l]!='+':
                                            bad_track = True
                                    if not bad_track:
                                        result += 1
                            else:
                                break
                    else:
                        break
    return result
