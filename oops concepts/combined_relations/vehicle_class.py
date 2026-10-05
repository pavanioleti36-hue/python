class Vehicle:
    def move(self):
        print("Vehicle is moving")
class Engine:
    def start(self):
        print("Engine starts")
class Car(Vehicle):
    def __init__(self):
        self.engine = Engine()
    def start_car(self):
        self.engine.start()
        self.move()
car = Car()
car.start_car()