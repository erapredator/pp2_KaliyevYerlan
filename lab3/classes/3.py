class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

length = int(input("Enter a width: "))
width = int(input("Enter a lenght: "))
rectangle = Rectangle(length, width)
print("Rectangle area:", rectangle.area())