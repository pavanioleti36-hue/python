class InvalidProductError(Exception):
    pass
class InvalidQuantityError(Exception):
    pass
class ShoppingCart:
    def __init__(self):
        self.products = {"Book": 100, "Pen": 10}
    def add_product(self, name, quantity):
        try:
            if name not in self.products:
                raise InvalidProductError("Product not found")
            if quantity <= 0:
                raise InvalidQuantityError("Quantity must be positive")
            print("Total price:", self.products[name] * quantity)
        except (InvalidProductError, InvalidQuantityError) as e:
            print(e)
cart = ShoppingCart()
cart.add_product("Book", 2)