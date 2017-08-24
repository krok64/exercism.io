def encode(phrase, num):
    line = []
    for i in range(num):
        line.append("")

    flag = 0
    dx = 1
    for pos, ch in enumerate(phrase):
        line[flag] += ch
        flag += dx
        if flag == num - 1:
            dx = -1
        if flag == 0:
            dx = 1

    return "".join(line)


def decode(phrase, num):
    line = [[]] * num
    for i in range(num):
        line[i] = []

    p_len = len(phrase)

    flag = 0
    dx = 1
    for _ in range(p_len):
        for i in range(num):
            if i == flag:
                line[i].append("?")
            else:
                line[i].append(".")
        flag += dx
        if flag == num - 1:
            dx = -1
        if flag == 0:
            dx = 1

    pos = 0
    for i in range(num):
        for j in range(p_len):
            if line[i][j] == "?":
                line[i][j] = phrase[pos]
                pos += 1

    result = ""
    for j in range(p_len):
        for i in range(num):
            if line[i][j] != ".":
                result += line[i][j]
                break
    return result
