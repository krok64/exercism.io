import re


class Phone():
    def __init__(self, num):
        self.number = re.sub("[ -.]", "", num)
        if len(self.number) == 11 and self.number[0] == "1":
            self.number = self.number[1:]
        if len(self.number) != 10:
            self.number = '0' * 10

    def area_code(self):
        return self.number[0:3]

    def pretty(self):
        return "(" + self.number[0:3] + ") " + self.number[3:6] + "-" + self.number[6:]