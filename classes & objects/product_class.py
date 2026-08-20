class product:
    category = "Electronics"
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def display_info(self):
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Category:", product.category)
product1 = product("Smartphone", 8000, 20)
product1.display_info()            