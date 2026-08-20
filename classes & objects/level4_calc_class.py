class Calculator:
    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"


calc = Calculator()

print("Addition:", calc.addition(10, 5))
print("Subtraction:", calc.subtraction(10, 5))
print("Multiplication:", calc.multiplication(10, 5))
print("Division:", calc.division(10, 5))
