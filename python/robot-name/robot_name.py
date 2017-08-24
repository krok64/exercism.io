import random
import string

old_names = []


class Robot():

    def __init__(self):
        self.name = self.new_name()

    def new_name(self):
        while 1:
            new = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + "%03d" % (random.randint(0, 999))
            if new not in old_names:
                break
        old_names.append(new)
        return new

    def reset(self):
        self.name = self.new_name()
