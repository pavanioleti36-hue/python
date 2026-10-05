class printer:
    def print(self, name):
        print("student name:", name)
class student:
    def __init__(self, name):
        self.name = name
    def show(self, printer):
        printer.print(self.name)
s= student("Pavani")
p= printer()
s.show(p)