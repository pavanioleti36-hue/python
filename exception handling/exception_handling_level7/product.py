class InsufficientStockError(Exception):
    pass
class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock
    def purchase(self, quantity):
        try:
            if quantity <= 0:
                raise ValueError("Quantity must be positive")
            if quantity > self.stock:
                raise InsufficientStockError("Insufficient stock")
            self.stock -= quantity
            print("Remaining stock:", self.stock)
        except (ValueError, InsufficientStockError) as e:
            print(e)
product = Product("Laptop", 5)
product.purchase(8)