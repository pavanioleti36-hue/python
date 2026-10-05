class Person:
    def speak(self):
        print("Person can speak")
class Teacher(Person):
    def teach(self):
        print("Teacher teaches students")
teacher = Teacher()
teacher.speak()
teacher.teach()