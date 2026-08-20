class calculator:
    def add(self, a, b):
        return a+b
    def sub(self, a, b):
        return a-b  
    def mul(self, a, b):
        return a*b
    def div(self, a, b):
        if b!=0:
           return a*b   
        else:
            print("Error: division by zero not allowed")
calc= calculator()            
print("Addition:", calc.add(10, 5))
print("Subtraction:", calc.sub(10, 5))
print("Multiplication:", calc.mul(10, 5))
print("Division:", calc.div(10, 5))
print("Division by zero:", calc.div(10, 0))