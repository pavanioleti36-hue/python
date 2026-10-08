from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @abstractmethod
    def role(self):
        pass
class Student(Person):
    def role(self):
        print("Student studies")
class Teacher(Person):
    def role(self):
        print("Teacher teaches")
class Doctor(Person):
    def role(self):
        print("Doctor treats patients")
Student("Pavani", 20).role()
Teacher("Ravi", 35).role()
Doctor("Sita", 40).role()