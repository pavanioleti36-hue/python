class engine:
    def start(self):
        print("Engine is starting")
class car:
    def __init__(self):
        self.engine = engine()
    def start_car(self):
        self.engine.start()
        print("Car is starting")
c= car()
c.start_car()