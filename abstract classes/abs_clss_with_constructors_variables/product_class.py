from abc import ABC, abstractmethod
class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    @abstractmethod
    def calculate_discount(self):
        pass
class Mobile(Product):
    def calculate_discount(self):
        return self.price * 0.10
p = Mobile("Phone", 20000)
print(p.name, p.price, p.calculate_discount())