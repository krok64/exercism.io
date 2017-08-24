import re


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({}:{})'.format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not(self == other)


class WordSearch(object):
    def __init__(self, arr):
        self.data = [x for x in arr.split("\n")]
        self.x_len = len(self.data[0])
        self.y_len = len(self.data)

    def search(self, word):
        w_len = len(word)
        for x in range(self.x_len):
            for y in range(self.y_len):
                if self.data[y][x]==word[0]:
                    p1 = Point(x, y)
                    #to the rigth
                    line = self.data[y][x:]
                    if check_for_word_in_line(word, line):
                        p2 = Point(x + w_len - 1, y)
                        return((p1, p2))
                    #to left
                    line = self.data[y][:x+1]
                    if check_for_word_in_line(word, line[::-1]):
                        p2 = Point(x - w_len + 1, y)
                        return((p1, p2))
                    #to top
                    line = "".join([self.data[a][x] for a in range(y, -1, -1)])
                    if check_for_word_in_line(word, line):
                        p2 = Point(x, y - w_len + 1)
                        return((p1, p2))
                    #to bottom
                    line = "".join([self.data[a][x] for a in range(y, self.y_len)])
                    if check_for_word_in_line(word, line):
                        p2 = Point(x, y + w_len - 1)
                        return((p1, p2))
                    #to 45gradus
                    line = ""
                    dx = 0
                    dy = 0
                    while 1:
                        line += self.data[y + dy][x + dx]
                        dx = dx + 1
                        dy = dy + 1
                        if (x + dx == self.x_len) or (y + dy == self.y_len):
                            break
                    if check_for_word_in_line(word, line):
                        p2 = Point(x + w_len - 1, y + w_len - 1)
                        return((p1, p2))
                    #to 135gradus
                    line = ""
                    dx = 0
                    dy = 0
                    while 1:
                        line += self.data[y + dy][x + dx]
                        dx = dx - 1
                        dy = dy + 1
                        if (x + dx == -1) or (y + dy == self.y_len):
                            break
                    if check_for_word_in_line(word, line):
                        p2 = Point(x - w_len + 1, y + w_len - 1)
                        return((p1, p2))
                    #to 225gradus
                    line = ""
                    dx = 0
                    dy = 0
                    while 1:
                        line += self.data[y + dy][x + dx]
                        dx = dx - 1
                        dy = dy - 1
                        if (x + dx == -1) or (y + dy == -1):
                            break
                    if check_for_word_in_line(word, line):
                        p2 = Point(x - w_len + 1, y - w_len + 1)
                        return((p1, p2))
                    #to 315gradus
                    line = ""
                    dx = 0
                    dy = 0
                    while 1:
                        line += self.data[y + dy][x + dx]
                        dx = dx + 1
                        dy = dy - 1
                        if (x + dx == self.x_len) or (y + dy == -1):
                            break
                    if check_for_word_in_line(word, line):
                        p2 = Point(x + w_len - 1, y - w_len + 1)
                        return((p1, p2))
        return None

def check_for_word_in_line(word, line):
    if len(word) > len(line):
        return False
    if re.search("^"+word, line):
        return True

if __name__ == '__main__':
    puzzle = ('jefblpepre\n'
                  'camdcimgtc\n'
                  'oivokprjsm\n'
                  'pbwasqroua\n'
                  'rixilelhrs\n'
                  'wolcqlirpc\n'
                  'screeaumgr\n'
                  'alxhpburyi\n'
                  'jalaycalmp\n'
                  'clojurermt')
    example = WordSearch(puzzle)
    print(example.search('ecmascript'))
