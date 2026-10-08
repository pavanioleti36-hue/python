from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    def display_info(self):
        print("Vehicle: Transportation Vehicle")
class Car(Vehicle):
    def start(self):
        print("Car starts")
class Bike(Vehicle):
    def start(self):
        print("Bike starts")
c = Car()
b = Bike()
c.start()
c.display_info()
b.start()
b.display_info()