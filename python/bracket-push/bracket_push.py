def check_brackets(phrase):
    bstack = []
    open_braces = "[{("
    close_braces = "]})"
    for i in phrase:
        if i in open_braces:
            bstack.append(i)
        elif i in close_braces:
            try:
                last = bstack.pop()
            except IndexError:
                return False
            if close_braces.find(i) != open_braces.find(last):
                return False
    if len(bstack) > 0:
        return False
    return True
