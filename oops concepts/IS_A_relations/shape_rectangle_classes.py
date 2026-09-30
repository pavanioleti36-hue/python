class shape:
    def shape_class(self):
        print("shapes have dimensions")
class rectangle(shape):
    def area(self):
        print("rectangle has area")
c= rectangle()
c.shape_class()
c.area()