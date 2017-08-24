def slices(phrase, num):
    if num == 0:
        raise ValueError
    if num > len(phrase):
        raise ValueError
    ret_list = []
    for i in range(len(phrase)-num+1):
        ret_ret_list=[]
        for j in phrase[i:i+num]:
        	ret_ret_list.append(int(j))
        ret_list.append(ret_ret_list)
    return ret_list
