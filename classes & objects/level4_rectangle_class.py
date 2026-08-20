class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


rect1 = Rectangle(10, 5)
rect2 = Rectangle(7, 3)

print("Rectangle 1 - Area:", rect1.area(), "Perimeter:", rect1.perimeter())
print("Rectangle 2 - Area:", rect2.area(), "Perimeter:", rect2.perimeter())

