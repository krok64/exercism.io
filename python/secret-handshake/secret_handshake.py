secret = {1: "wink", 0b10:"double blink", 0b100: "close your eyes", 0b1000: "jump"}


def handshake(code):
    if isinstance(code, str):
        try:
            code = int(code, 2)
        except ValueError:
            return []
    if code < 1:
        return []
    result = []
    for i in sorted(secret):
        if i & code:
            result.append(secret[i])
    if code & 0b10000:
        result = result[::-1]
    return result


def code(phrase):
    result = 0
    reversed = False
    prev = -1
    for code in phrase:
        found = False
        for num, word in zip(secret.keys(), secret.values()):
            if word == code:
                result += num
                if prev > num:
                    reversed = True
                prev = num
                found = True
                break
        if not found:
            return str(0)
    if reversed:
        result += 0b10000
    return(format(result, 'b'))

