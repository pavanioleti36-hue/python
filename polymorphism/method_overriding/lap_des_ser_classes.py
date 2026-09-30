class computer:
    def process(self):
        print("It is a computer classes")
class laptop(computer):
    def process(self):
        print("It is a laptop class")
class desktop(computer):
    def process(self):
        print("It is a desktop class")
class server(computer):
    def area(self):
        print("It is a server class")
l= laptop()
d= desktop()
s= server()
l.process()
d.process()
s.process()