from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self, color):
        self.color = color
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
c = Circle("Red", 5)
print(c.color, c.area())