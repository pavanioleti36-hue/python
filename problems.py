class pavani:
    def __init__(self, name, pin , branch):
        self.name = name
        self.pin = pin
        self.branch = branch

    def display(self):
        print("Name:", self.name)
        print("Pin:", self.pin)
        print("Branch:", self.branch)
s1 = pavani("Pavani", 169 , "cse")
s1.display()