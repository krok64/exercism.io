SUBLIST, SUPERLIST, EQUAL, UNEQUAL = range(4)


def check_lists(list1, list2):
    len1 = len(list1)
    len2 = len(list2)

    if (len1 < len2 and find_sub_list(list2, list1)) or (len1 < len2 and list1 == []):
        return SUBLIST
    elif (len1 > len2 and find_sub_list(list1, list2)) or (len1 > len2 and list2 == []):
        return SUPERLIST
    elif find_sub_list(list1, list2) or list1 == list2:
        return EQUAL
    else:
        return UNEQUAL


def find_sub_list(list1, list2):
    j = 0
    for i in range(len(list1) - len(list2) + 1):
        for j in range(len(list2)):
            if list1[i + j] != list2[j]:
                break
            if j == len(list2) - 1:
                return True
    return False
