class Car:
    def start(self):
        print("Car starts with a key")
class Bike:
    def start(self):
        print("Bike starts with a key")
class Bus:
    def start(self):
        print("Bus starts with a key")
def start_vehicle(vehicle):
    vehicle.start()
car = Car()
bike = Bike()
bus = Bus()
start_vehicle(car)
start_vehicle(bike)
start_vehicle(bus)