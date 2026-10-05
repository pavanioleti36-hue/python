class Vehicle:
    def start(self):
        print("Vehicle starts")
class Car(Vehicle):
    def drive(self):
        print("Car is driving")
class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")
class Bus(Vehicle):
    def travel(self):
        print("Bus is traveling")
c = Car()
b = Bike()
bus = Bus()
c.start()
c.drive()
b.start()
b.ride()
bus.start()
bus.travel()