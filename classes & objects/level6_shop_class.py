class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_product(self, name, price, quantity=1):
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"price": price, "quantity": quantity}

    def remove_product(self, name, quantity=1):
        if name in self.items:
            self.items[name]["quantity"] -= quantity
            if self.items[name]["quantity"] <= 0:
                del self.items[name]

    def calculate_total(self):
        total = 0
        for item in self.items.values():
            total += item["price"] * item["quantity"]
        return total


# Example usage
cart = ShoppingCart()
cart.add_product("Laptop", 50000, 1)
cart.add_product("Phone", 20000, 2)
cart.add_product("Headphones", 1500, 3)

print("Total before removal: " + str(cart.calculate_total()))

cart.remove_product("Phone", 1)
print("Total after removing 1 Phone: " + str(cart.calculate_total()))
