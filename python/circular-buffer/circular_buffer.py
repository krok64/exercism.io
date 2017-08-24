class CircularBuffer():
    def __init__(self, size):
        self.size = size
        self.buff = []

    def read(self):
        if len(self.buff) == 0:
            raise BufferEmptyException
        return self.buff.pop(0)

    def write(self, num):
        if len(self.buff) == self.size:
            raise BufferFullException
        self.buff.append(num)

    def clear(self):
        self.buff = []

    def overwrite(self, num):
        if len(self.buff) == self.size:
            self.buff.pop(0)
            self.buff.append(num)
        else:
            self.buff.append(num)


class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass