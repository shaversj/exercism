# Globals for the bearings
# Change the values as you see fit

EAST = "EAST"
NORTH = "NORTH"
WEST = "WEST"
SOUTH = "SOUTH"


class Robot(object):
    directions = ["NORTH", "EAST", "SOUTH", "WEST"]

    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.x = x
        self.y = y

    @property
    def coordinates(self):
        return (self.x, self.y)

    def turn_right(self):
        index = self.directions.index(self.bearing)
        try:
            new_bearing = self.directions[index + 1]
        except IndexError:
            new_bearing = self.directions[0]

        self.bearing = new_bearing

    def turn_left(self):
        index = self.directions.index(self.bearing)
        try:
            new_bearing = self.directions[index - 1]
        except IndexError:
            new_bearing = self.directions[-1]

        self.bearing = new_bearing

    def simulate(self, instructions):
        for instruction in instructions:
            if instruction == "R":
                self.turn_right()
            if instruction == "L":
                self.turn_left()
            if instruction == "A":
                self.advance()

    def advance(self):
        if self.bearing == "NORTH":
            self.y += 1
        if self.bearing == "SOUTH":
            self.y -= 1
        if self.bearing == "EAST":
            self.x += 1
        if self.bearing == "WEST":
            self.x -= 1
