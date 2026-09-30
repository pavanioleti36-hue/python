class person:
    def role(self):
        print("person plays a role")
class student(person):
    def role(self):
        print("person plays student role")
class teacher(person):
    def role(self):
        print("person plays teacher role")
class doctor(person):
    def role(self):
        print("person plays doctor role")
s= student()
t= teacher()
d= doctor()
s.role()
t.role()
d.role()