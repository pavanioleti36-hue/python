class Employee:
    def __init__(self, salary):
        self.salary = salary
    def __gt__(self, other):
        return self.salary > other.salary
e1 = Employee(50000)
e2 = Employee(40000)
print(e1 > e2)