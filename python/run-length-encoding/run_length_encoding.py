def decode(phrase):
    out_str=""
    num = 0
    for ch in phrase:
        if ch.isdigit():
            num = num * 10 + int(ch)
        else:
            if num>0:
                out_str = out_str + num * ch
                num = 0
            else:
                out_str = out_str + ch
    return out_str

def encode(phrase):
    prev_ch = False
    count = 0
    out_str=""
    for ch in phrase:
        if ch==prev_ch:
            count += 1
        else:
            if prev_ch != False:
                if count>1:
                    out_str = out_str + str(count) + prev_ch
                else:
                    out_str = out_str + prev_ch
            count = 1
        prev_ch = ch

    if prev_ch != False:
        if count>1:
            out_str = out_str + str(count) + prev_ch
        else:
            out_str = out_str + prev_ch
    count = 1
    return out_str

