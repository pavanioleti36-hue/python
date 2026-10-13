class InvalidProductError(Exception): pass
class InsufficientStockError(Exception): pass
class InvalidQuantityError(Exception): pass
class ShoppingCart:
    def __init__(self):
        self.products = {"Book": {"price": 100, "stock": 5}, "Pen": {"price": 10, "stock": 20}}
    def add_product(self, name, quantity):
        try:
            if name not in self.products:
                raise InvalidProductError("Product not found")
            if quantity <= 0:
                raise InvalidQuantityError("Quantity must be positive")
            product = self.products[name]
            if quantity > product["stock"]:
                raise InsufficientStockError("Insufficient stock")
            product["stock"] -= quantity
            print("Total price:", product["price"] * quantity)
        except (InvalidProductError, InvalidQuantityError, InsufficientStockError) as e:
            print(e)
cart = ShoppingCart()
cart.add_product("Book", 2)
cart.add_product("Pen", 0)