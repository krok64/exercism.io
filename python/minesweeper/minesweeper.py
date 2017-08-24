def board(brd):
    cols = len(brd[0])
    rows = len(brd)
    for i in range(1, rows):
        if len(brd[i]) != cols:
            raise ValueError("different len")
    if brd[0][0] != "+" or brd[0][cols-1] != "+" or brd[rows-1][0] != "+" or brd[rows-1][cols-1] != "+":
        raise ValueError("wrong angles")
    for i in range (1, cols - 1):
        if brd[0][i] != "-" or brd[rows-1][i] != "-":
            raise ValueError("wrong - sides")
    for i in range (1, rows - 1):
        if brd[i][0] != "|" or brd[i][cols-1] != "|":
            raise ValueError("wrong | sides")
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if brd[i][j] == "*":
                continue
            elif brd[i][j] == " ":
                bombs = 0
                for i_2 in range(i-1, i+2):
                    for j_2 in range(j-1, j+2):
                        if i_2 < 0 or j_2 < 0 or i_2 >= rows - 1 or j_2 >= cols - 1:
                            continue
                        if brd[i_2][j_2] == "*":
                            bombs += 1
                if bombs > 0:
                    brd[i] = brd[i][:j] + str(bombs) + brd[i][j + 1:]
            else:
                raise ValueError("wrong symbol")
    return brd
