class Laptop:
    def __init__(self, brand, model, processor, ram, storage, graphics, os):
        self.brand = brand
        self.model = model
        self.processor = processor
        self.ram = ram
        self.storage = storage
        self.graphics = graphics
        self.os = os

    def display_specs(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Processor:", self.processor)
        print("RAM:", self.ram)
        print("Storage:", self.storage)
        print("Graphics:", self.graphics)
        print("Operating System:", self.os)
        print("-------------------------")

laptop1 = Laptop("Dell", "XPS 15", "Intel i7", "16GB", "512GB SSD", "NVIDIA GTX 1650", "Windows 11")
laptop2 = Laptop("HP", "Pavilion", "Intel i5", "8GB", "1TB HDD", "Intel UHD Graphics", "Windows 10")
laptop3 = Laptop("Apple", "MacBook Air", "Apple M1", "8GB", "256GB SSD", "Integrated", "macOS Monterey")

laptop1.display_specs()
laptop2.display_specs()
laptop3.display_specs()
