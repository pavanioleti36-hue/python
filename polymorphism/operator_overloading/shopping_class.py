class ShoppingCart:
    def __init__(self, items):
        self.items = items
    def __add__(self, other):
        return ShoppingCart(self.items + other.items)
cart1 = ShoppingCart(["Book", "Pen"])
cart2 = ShoppingCart(["Bag", "Bottle"])
cart3 = cart1 + cart2
print("Combined Cart:", cart3.items)