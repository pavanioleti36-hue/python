class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

rect1 = Rectangle(10, 5)
rect2 = Rectangle(7, 3)
rect3 = Rectangle(12, 8)

print("Rectangle 1 Area:", rect1.get_area())
print("Rectangle 2 Area:", rect2.get_area())
print("Rectangle 3 Area:", rect3.get_area())