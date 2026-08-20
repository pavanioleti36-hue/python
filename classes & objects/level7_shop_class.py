class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_product(self, name, price, quantity=1):
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"price": price, "quantity": quantity}

    def calculate_total(self):
        total = 0
        for item in self.items.values():
            total += item["price"] * item["quantity"]
        return total

    def show_cart(self):
        cart_details = ""
        for name, details in self.items.items():
            cart_details += name + " - ₹" + str(details["price"]) + " x " + str(details["quantity"]) + "\n"
        return cart_details if cart_details else "Cart is empty"


cart = ShoppingCart()
cart.add_product("Laptop", 50000, 1)
cart.add_product("Phone", 20000, 2)
cart.add_product("Headphones", 1500, 3)

print("Cart contents:\n" + cart.show_cart())
print("Total bill: ₹" + str(cart.calculate_total()))
