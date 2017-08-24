class Clock():
    def __init__(self, h, m):
        self.h = h
        self.m = m

    def __str__(self):
        h = self.h
        m = self.m
        if m >= 60:
            m2 = m % 60
            dh = (m - m2) / 60
            h += dh
            m = m2
        if m < 0:
            m2 = m % 60
            dh = (m - m2) / 60
            h += dh
            m = m2
        if h < 0:
            h = 24 + h % 24 
        if h >= 24:
            h = h % 24
        return "%02d:%02d" % (h, m)

    def __repr__(self):
        return self.__str__()

    def add(self, min):
        self.m += min
        return self.__str__()

    def __eq__(self, other):
        if self.__str__() == other.__str__():
            return True
        return False
