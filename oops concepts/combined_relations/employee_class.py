class Employee:
    def work(self):
        print("Employee is working")
class Laptop:
    def start(self):
        print("Laptop starts")
class Developer(Employee):
    def __init__(self):
        self.laptop = Laptop()
    def develop(self):
        self.laptop.start()
        print("Developer writes code")
developer = Developer()
developer.work()
developer.develop()