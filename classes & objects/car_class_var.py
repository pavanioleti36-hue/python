class car:
    company= "mahindra"
    no_of_wheels= 4
    def __init__(self, model, price):
        self.model= model
        self.price= price
    def display(self):
        print("car company:",car.company)
        print("car model:",self.model)
        print("car price:",self.price)
        print("no.of wheels:",car.no_of_wheels)
car1= car("BMW", 500000)
car2= car("range rover", 600000)    
car1.display()
car2.display()    