from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def display_shape(self):
        print("This is a shape")
class Circle(Shape):
    def area(self):
        print("Circle Area:", 3.14 * 5 * 5)
class Rectangle(Shape):
    def area(self):
        print("Rectangle Area:", 10 * 3)
c = Circle()
r = Rectangle()
c.area()
c.display_shape()
r.area()
r.display_shape()