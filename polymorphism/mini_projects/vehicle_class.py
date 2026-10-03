class Car:
    def start(self):
        print("Car starts with a key")
class Bike:
    def start(self):
        print("Bike starts with a self-start button")
class Bus:
    def start(self):
        print("Bus starts with a key")
class Truck:
    def start(self):
        print("Truck starts with a key")
vehicles = [Car(), Bike(), Bus(), Truck()]
for vehicle in vehicles:
    vehicle.start()