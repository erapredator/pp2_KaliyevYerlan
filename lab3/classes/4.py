import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

p1 = Point(1, 2)
p2 = Point(4, 6)

print("Point 1:")
p1.show()

print("Point 2:")
p2.show()

print("Move Point 1 by 2 in the x direction and 3 in the y direction:")
p1.move(2, 3)
p1.show()

print("The distance between Point 1 and Point 2:")
print(p1.dist(p2))
