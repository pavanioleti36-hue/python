class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False  # Track car state

    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.brand} {self.model} started.")
        else:
            print(f"{self.brand} {self.model} is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"{self.brand} {self.model} stopped.")
        else:
            print(f"{self.brand} {self.model} is already stopped.")

    def display_details(self):
        print(f"Car: {self.year} {self.brand} {self.model}, Running: {self.is_running}")

car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Tesla", "Model 3", 2023)

car1.display_details()
car1.start()
car1.display_details()
car1.stop()
car1.display_details()

car2.display_details()
car2.start()
car2.stop()
