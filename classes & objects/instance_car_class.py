class car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
    def display(self):
        print("Car Brand:", self.brand)
        print("Car Model:", self.model)
        print("Car Year:", self.year)
        print("Car Price:", self.price)
car1 = car("BMW", "X5", 2022, 50000)
car2= car("Audi", "A6", 2021, 45000)
car1.display()
car2.display()