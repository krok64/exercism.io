def encode(arr):
    result = []
    for num in arr:
        if num < 0x80:
            result.append(num)
        else:
            num_lst = []
            while num > 0:
                temp = num & 0b1111111
                num = num >> 7
                if len(num_lst) == 0:
                    num_lst.append(temp)
                else:
                    num_lst.append(temp | 0b10000000)
            result.extend(num_lst[::-1])
    return result


def decode(arr):
    result = []
    curr_num = 0
    begindecode = False
    for num in arr:
        if num & 0b10000000:
            curr_num = (curr_num << 7) + (num & 0b01111111)
            begindecode = True
        else:
            curr_num = (curr_num << 7) + num
            result.append(curr_num)
            curr_num = 0
            begindecode = False
    if begindecode:
        raise ValueError
    return result
