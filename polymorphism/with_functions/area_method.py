class Circle:
    def area(self):
        radius = 5
        return 3.14 * radius * radius
class Rectangle:
    def area(self):
        length = 10
        width = 5
        return length * width
class Triangle:
    def area(self):
        base = 10
        height = 6
        return 0.5 * base * height
def calculate_area(shape):
    print("Area =", shape.area())
c = Circle()
r = Rectangle()
t = Triangle()
calculate_area(c)
calculate_area(r)
calculate_area(t)