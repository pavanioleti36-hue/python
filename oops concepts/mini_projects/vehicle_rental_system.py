class Vehicle:
    def __init__(self,name):
        self.name=name
class Car(Vehicle):
    def type(self):
        print("Car:",self.name)
class Bike(Vehicle):
    def type(self):
        print("Bike:",self.name)
class Customer:
    def __init__(self,name):
        self.name=name
class PaymentService:
    def pay(self,amount):
        print("Rental payment:",amount)
class Rental:
    def __init__(self,customer,vehicle):
        self.customer=customer
        self.vehicle=vehicle
    def rent(self,service,amount):
        service.pay(amount)
customer=Customer("Pavani")
car=Car("Toyota")
rental=Rental(customer,car)
car.type()
rental.rent(PaymentService(),3000)