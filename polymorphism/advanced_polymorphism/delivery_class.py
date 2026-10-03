class Delivery:
    def calculate_delivery_charge(self):
        pass
class LocalDelivery(Delivery):
    def calculate_delivery_charge(self):
        return 50
class ExpressDelivery(Delivery):
    def calculate_delivery_charge(self):
        return 100
class InternationalDelivery(Delivery):
    def calculate_delivery_charge(self):
        return 500
# Creating objects
local = LocalDelivery()
express = ExpressDelivery()
international = InternationalDelivery()
print("Local Delivery Charge:", local.calculate_delivery_charge())
print("Express Delivery Charge:", express.calculate_delivery_charge())
print("International Delivery Charge:", international.calculate_delivery_charge())