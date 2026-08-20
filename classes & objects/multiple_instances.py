class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number * self.number

    def double_square(self):
        return 2 * self.square()


calc1 = Calculator(5)
print("Square:", str(calc1.square()))
print("Double of square:", str(calc1.double_square()))
