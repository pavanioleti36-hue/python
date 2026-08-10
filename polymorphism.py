class lion:
    def sound(self):
        print("lion roars")
class dog:
    def sound(self):
        print("dog barks")
class baby:
    def sound(self):
        print("baby cries")
l=lion()
d=dog()
b=baby()
def animal_sound(animal):
    animal.sound()
animal_sound(l)
animal_sound(d)
animal_sound(b)            