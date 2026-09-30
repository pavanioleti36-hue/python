class person:
    def details(self):
        print("person has details")
class student(person):
    def name(self):
        print("student have name")
c= student()
c.details()
c.name()