def can_attack(poz1, poz2):
    if (not check_pozition(poz1)) or (not check_pozition(poz2)) or poz1==poz2:
        raise ValueError("wrong position")
    if poz1[0]==poz2[0] or poz1[1]==poz2[1] or abs(poz1[0]-poz2[0])==abs(poz1[1]-poz2[1]):
        return True
    return False


def check_pozition(poz):
    if poz[0]<0 or poz[1]<0 or poz[0]>7 or poz[1]>7:
        return False
    return True


def board(poz1, poz2):
    if (not check_pozition(poz1)) or (not check_pozition(poz2)) or poz1 == poz2:
        raise ValueError("wrong position")
    result = ["_" * 8 for i in range(8)]
    result[poz1[0]] = str_change_char(result[poz1[0]], poz1[1], "W")
    result[poz2[0]] = str_change_char(result[poz2[0]], poz2[1], "B")
    return result


def str_change_char(s, poz, char):
    return s[:poz] + char + s[poz + 1:]
