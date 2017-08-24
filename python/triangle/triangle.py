class TriangleError(Exception):
    pass

class Triangle():
    def __init__(self, a, b, c):
        t_list = sorted([a, b, c])
        if t_list[2] >= t_list[0] + t_list[1]:
            raise TriangleError
        if a == b == c:
            self.tip = "equilateral"
        elif a == b or b == c or c == a:
            self.tip = "isosceles"
        else:
            self.tip = "scalene"

    def kind(self):
        return self.tip
