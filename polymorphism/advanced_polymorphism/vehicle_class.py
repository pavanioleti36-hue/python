from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    def stop(self):
        pass
class Car(vehicle):
    def start(self):
        print("Car started")
class Bike(vehicle):
    def start(self):
        print("Bike started")
    def stop(self):
        print("Bike stopped")
class Bus(vehicle):
    def start(self):
        print("Bus started")
    def stop(self):
        print("Bus stopped")
c= Car()
b = Bike()
bus = Bus()
c.start()
c.stop()
b.start()
b.stop()
bus.start()
bus.stop()
