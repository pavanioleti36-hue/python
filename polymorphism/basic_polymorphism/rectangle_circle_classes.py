class rectangle:
    def area(self, length, breadth):
        print("length of the rectangle : ", length * breadth)
class circle:
    def area(self, radius):
        print("Area of the circle : ", 3.14 * radius * radius)
r= rectangle()
c= circle()
area= r.area(10, 20)
area= c.area(5)                