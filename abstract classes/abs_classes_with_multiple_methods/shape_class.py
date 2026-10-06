from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Circle(Shape):
    def area(self):
        radius = 5
        print("Circle Area:", 3.14 * radius * radius)

    def perimeter(self):
        radius = 5
        print("Circle Perimeter:", 2 * 3.14 * radius)
class rectangle(Shape):
    def area(self):
        length = 10
        width = 5
        print("Rectangle Area:", length * width)

    def perimeter(self):
        length = 10
        width = 5
        print("Rectangle Perimeter:", 2 * (length + width))
c= Circle()
r= rectangle()
c.area()
c.perimeter()
r.area()
r.perimeter()