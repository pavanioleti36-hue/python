class Employee:
    def work(self):
        print("Employee is working")
class Developer(Employee):
    def code(self):
        print("Developer writes code")
class Tester(Employee):
    def test(self):
        print("Tester tests the software")
class Manager(Employee):
    def manage(self):
        print("Manager manages the team")
d = Developer()
t = Tester()
m = Manager()
d.work()
d.code()
t.work()
t.test()
m.work()
m.manage()