class LinkedList():
    def __init__(self):
        self.lst = []

    def __iter__(self):
        for a in self.lst:
            yield a

    def __len__(self):
        return len(self.lst)

    def push(self, val):
        self.lst.append(val)

    def unshift(self, val):
        self.lst.insert(0, val)

    def pop(self):
        return self.lst.pop()

    def shift(self):
        return self.lst.pop(0)