class duck:
    def  walk(self):
        print("duck is walking")
class dog:
    def walk(self):
        print("dog is walking")
def make_walk(obj):
    obj.walk()
duck= duck()
dog= dog()
make_walk(duck)
make_walk(dog)                 