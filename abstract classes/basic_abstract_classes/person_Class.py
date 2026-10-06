from abc import ABC, abstractmethod
class Person(ABC):
    @abstractmethod
    def role(self):
        pass
class Student(Person):
    def role(self):
        print("Role: Student")
class Teacher(Person):
    def role(self):
        print("Role: Teacher")
s = Student()
t = Teacher()
s.role()
t.role()