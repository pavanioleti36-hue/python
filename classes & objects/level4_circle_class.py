import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

circle1 = Circle(3)
circle2 = Circle(6)

print("Circle 1 - Area:", circle1.area(), "Circumference:", circle1.circumference())
print("Circle 2 - Area:", circle2.area(), "Circumference:", circle2.circumference())

