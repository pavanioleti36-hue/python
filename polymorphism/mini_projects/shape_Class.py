class Circle:
    def area(self):
        return 3.14 * 5 * 5
class Rectangle:
    def area(self):
        return 10 * 5
class Square:
    def area(self):
        return 5 * 5
class Triangle:
    def area(self):
        return 0.5 * 8 * 6
shapes = [Circle(), Rectangle(), Square(), Triangle()]
for shape in shapes:
    print("Area:", shape.area())