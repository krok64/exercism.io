import re

class Luhn(object):
    def __init__(self, num):
        if len(num)<1:
            raise ValueError
        self.num = re.sub(" ","",num)
        if re.search("\D", self.num) or len(num)==1:
            self.invalid = True
        else:
            self.invalid = False


    def is_valid(self):
        if self.invalid:
            return False
        summa = sum([int(x) for x in self.num[::-2]])
        for j in self.num[-2::-2]:
            k = int(j) * 2
            if k>9:
                k=k-9
            summa = summa + k
        if summa % 10 == 0:
            return True
        else:
            return False

