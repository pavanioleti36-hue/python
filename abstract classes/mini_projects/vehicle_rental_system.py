from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, vehicle_number, brand):
        self.vehicle_number = vehicle_number
        self.brand = brand

    @abstractmethod
    def calculate_rent(self, days):
        pass

    def display_vehicle(self):
        print("Vehicle Number:", self.vehicle_number)
        print("Brand:", self.brand)

class Car(Vehicle):
    def calculate_rent(self, days):
        return days * 1500

class Bike(Vehicle):
    def calculate_rent(self, days):
        return days * 500

class Truck(Vehicle):
    def calculate_rent(self, days):
        return days * 2500

vehicles = [
    Car("CAR101", "Toyota"),
    Bike("BIKE101", "Honda"),
    Truck("TRUCK101", "Tata")
]

for vehicle in vehicles:
    vehicle.display_vehicle()
    print("Rent for 3 days:", vehicle.calculate_rent(3))
    print()