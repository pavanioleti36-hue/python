class product:
    def __init__(self, name, price):
        self.name= name
        self.price=price
    def total(self, quantity):
        return self.price * quantity   
product1= product("TV",23000)
product2=product("fan", 200)
print(product1.name," total price with quantity of 2 is",str(product1.total(2)))     
print(product2.name," total price with quantity of 5 is",str(product2.total(5)))     