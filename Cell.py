class Cell():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash((self.x, self.y))
    def __str__(self):
        return "("+str(self.x) + "," + str(self.y) + ")"
    