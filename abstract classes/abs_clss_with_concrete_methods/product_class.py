from abc import ABC, abstractmethod
class Product(ABC):
    @abstractmethod
    def calculate_discount(self):
        pass
    def display_product(self):
        print("Product: Laptop")
class Electronics(Product):
    def calculate_discount(self):
        print("Discount: 10%")
class Clothing(Product):
    def calculate_discount(self):
        print("Discount: 20%")
e = Electronics()
c = Clothing()
e.calculate_discount()
e.display_product()
c.calculate_discount()
c.display_product()