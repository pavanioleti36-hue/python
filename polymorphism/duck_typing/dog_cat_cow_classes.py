class  dog:
    def sound(self):
        print("dog is domestic animal")
class cat:
    def sound(self):
        print("cat is domestic animal")
class cow:
    def sound(self):
        print("cow is domestic animal")
def obj_cls(obj):
    obj.sound()
d= dog()
c= cat()
co= cow()
obj_cls(d)
obj_cls(c)
obj_cls(co)                    