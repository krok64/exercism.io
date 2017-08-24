def transpose(inp):
    mas = inp.split("\n")
    result = []
    cols = 0
    rows = len(mas)
    for i in range(rows):
        if len(mas[i]) > cols:
            cols = len(mas[i])

    for i in range(cols):
        elem = ""
        for j in range(rows):
            try:
                a = mas[j][i]
            except IndexError:
                a = " "
            elem += a
        result.append(elem)

    return ("\n".join(result)).rstrip()