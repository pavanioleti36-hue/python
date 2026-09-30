class  car:
    def start(self):
        print("car is starting")
class bike:
    def start(self):
        print("bike is starting")
def obj_cls(obj):
    obj.start()
c= car()
b= bike()
obj_cls(c)
obj_cls(b)                    