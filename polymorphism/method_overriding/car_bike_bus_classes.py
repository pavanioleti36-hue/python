class vehicle:
    def start(self):
        print("vehicle is starting")
class car(vehicle):
    def start(self):
        print("car is starting")
class bike(vehicle):
    def start(self):
        print("bike is starting")
class bus(vehicle):
    def start(self):
        print("bus is stsrting")
car = car()
bike= bike()
bus = bus()
veh= vehicle()
car.start()
bike.start()
bus.start()
veh.start()