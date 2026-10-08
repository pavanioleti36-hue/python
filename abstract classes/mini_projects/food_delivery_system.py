from abc import ABC, abstractmethod

class Delivery(ABC):
    def __init__(self, distance):
        self.distance = distance

    @abstractmethod
    def calculate_charge(self):
        pass

    @abstractmethod
    def deliver(self):
        pass

class BikeDelivery(Delivery):
    def calculate_charge(self):
        return self.distance * 10

    def deliver(self):
        print("Food delivered by Bike")

class CarDelivery(Delivery):
    def calculate_charge(self):
        return self.distance * 20

    def deliver(self):
        print("Food delivered by Car")

class DroneDelivery(Delivery):
    def calculate_charge(self):
        return self.distance * 30

    def deliver(self):
        print("Food delivered by Drone")

deliveries = [
    BikeDelivery(5),
    CarDelivery(5),
    DroneDelivery(5)
]

for delivery in deliveries:
    delivery.deliver()
    print("Delivery Charge:", delivery.calculate_charge())
    print()