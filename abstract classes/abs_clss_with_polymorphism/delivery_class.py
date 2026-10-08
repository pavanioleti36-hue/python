from abc import ABC, abstractmethod
class Delivery(ABC):
    @abstractmethod
    def calculate_charge(self):
        pass
class StandardDelivery(Delivery):
    def calculate_charge(self):
        print("Standard Delivery Charge: 50")
class ExpressDelivery(Delivery):
    def calculate_charge(self):
        print("Express Delivery Charge: 100")
class SameDayDelivery(Delivery):
    def calculate_charge(self):
        print("Same Day Delivery Charge: 150")
deliveries = [StandardDelivery(), ExpressDelivery(), SameDayDelivery()]
for delivery in deliveries:
    delivery.calculate_charge()