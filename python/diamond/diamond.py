def make_diamond(letter):
    rebro = (ord(letter) - ord("A")) + 1 
    rows = rebro * 2 - 1
    result = []
    for i in range(rebro):
        if i==0:
            spaces = int((rows - 1) / 2)
            line = " " * spaces + "A" + " " * spaces + "\n"
        else:
            spaces_1 = rebro - 1 - i
            spaces_2 = rows - spaces_1 * 2 - 2
            line = " " * spaces_1 + chr(i+ord("A")) + " " * spaces_2 + chr(i+ord("A")) + " " * spaces_1 + "\n"
        result.append(line)
    a = result[:-1]
    a = a[::-1]
    result.extend(a)

    return "".join(result)