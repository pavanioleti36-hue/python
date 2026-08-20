class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        self.is_running = True
        print(self.brand + " " + self.model + " started")

    def stop(self):
        self.is_running = False
        print(self.brand + " " + self.model + " stopped")

    def display(self):
        print("Brand: " + self.brand)
        print("Model: " + self.model)
        print("Year: " + str(self.year))
        print("Running: " + str(self.is_running))


car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Tesla", "Model 3", 2023)

car1.display()
car1.start()
car1.display()
car1.stop()
car1.display()

print()

car2.display()
car2.start()
car2.display()
car2.stop()
car2.display()
