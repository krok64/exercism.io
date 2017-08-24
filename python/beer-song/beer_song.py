def verse(num):
    if num == 0:
        return "No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.\n"
    s1 = get_bottle_name(num)
    s2 = get_bottle_name(num - 1)
    if num == 1:
        it = "it"
    else:
        it = "one"
    return "%s of beer on the wall, %s of beer.\nTake %s down and pass it around, %s of beer on the wall.\n" % (s1, s1, it, s2)


def get_bottle_name(num):
    if num == 1:
        return "1 bottle"
    elif num == 0:
        return "no more bottles"
    else:
        return "%d bottles" % num


def song(first, last=0):
    result = ""
    for i in range(first, last - 1, -1):
        result += verse(i) + "\n"
    return result
