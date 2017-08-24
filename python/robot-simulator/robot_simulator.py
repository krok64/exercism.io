NORTH=0 
EAST=1 
SOUTH=2 
WEST=3

class Robot(object):
    def __init__(self, dir=NORTH, x=0, y=0):
        self.dir = dir
        self.x = x
        self.y = y

    @property
    def coordinates(self):
        return self.x, self.y

    @property
    def bearing(self):
        return self.dir

    def turn_right(self):
        self.dir += 1
        if self.dir==4:
            self.dir=0

    def turn_left(self):
        self.dir -= 1
        if self.dir==-1:
            self.dir=3

    def advance(self):
        if self.dir == NORTH:
            self.y += 1
        elif self.dir == EAST:
            self.x += 1
        elif self.dir == SOUTH:
            self.y -= 1
        elif self.dir == WEST:
            self.x -= 1

    def simulate(self, sim_str):
        for command in sim_str:
            if command=="L":
                self.turn_left()
            elif command=="R":
                self.turn_right()
            elif command=="A":
                self.advance()
