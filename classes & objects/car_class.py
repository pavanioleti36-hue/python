class Car:
    number_of_wheels = 4

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print("Brand: " + self.brand)
        print("Model: " + self.model)
        print("Number of Wheels: " + str(Car.number_of_wheels))
        print("-" * 25)


car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")
car3 = Car("Hyundai", "i20")

car1.display_info()
car2.display_info()
car3.display_info()
