def flatten(arr):
    ret_list = []
    if arr==None:
        return None
    if (not isinstance(arr, list)) and (not isinstance(arr, tuple)):
        ret_list = []
        ret_list.append(arr)
        return ret_list
    for elem in arr:
        if elem==None or elem==[] or elem==():
            continue
        if not isinstance(elem, list):
            ret_list.append(elem)
            continue
        a=flatten(elem)
        if a!=None:
            ret_list.extend(flatten(elem))
    return ret_list

