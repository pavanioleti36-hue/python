from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @abstractmethod
    def work(self):
        pass
class Manager(Employee):
    def work(self):
        print("Manager manages the team")
class Developer(Employee):
    def work(self):
        print("Developer writes code")
class Tester(Employee):
    def work(self):
        print("Tester tests software")
Manager("Ravi", 60000).work()
Developer("Sita", 50000).work()
Tester("Kumar", 45000).work()