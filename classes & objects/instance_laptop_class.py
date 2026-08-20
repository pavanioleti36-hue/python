class laptop:
    def __init__(self, brand, ram, processor, price):
        self.brand = brand
        self.ram = ram
        self.processor = processor
        self.price = price
    def display(self):
        print("Laptop Brand:", self.brand)
        print("Laptop RAM:", self.ram)
        print("Laptop Processor:", self.processor)
        print("Laptop Price:", self.price)
laptop1 = laptop("Dell", "16GB", "Intel i7", 1200)
laptop2 = laptop("HP", "8GB", "Intel i5", 800)
laptop3 = laptop("Lenovo", "32GB", "Intel i9", 1500)
laptop1.display()            
laptop2.display()
laptop3.display()