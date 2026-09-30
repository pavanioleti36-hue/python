class shape:
    def area(self):
        print("It is a shape class")
class rectangle(shape):
    def area(self):
        print("It is a rectangle class")
class circle(shape):
    def area(self):
        print("It is a circle class")
class triangle(shape):
    def area(self):
        print("It is a triangle class")
rec= rectangle()
cir= circle()
tri= triangle()
rec.area()
cir.area()
tri.area()