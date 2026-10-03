from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @abstractmethod
    def work(self):
        pass
    def __add__(self, other):
        return self.salary + other.salary
class Developer(Employee):
    def work(self):
        print(self.name, "is developing software")
class Tester(Employee):
    def work(self):
        print(self.name, "is testing software")
class Manager:
    def work(self):
        print("Manager is managing the team")
def do_work(employee):
    employee.work()
developer = Developer("Ravi", 50000)
tester = Tester("Anil", 40000)
manager = Manager()
developer.work()
tester.work()
do_work(manager)
# Operator overloading
total_salary = developer + tester
print("Combined Salary:", total_salary)