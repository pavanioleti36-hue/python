class InvalidChoiceError(Exception): pass
def divide():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        result = a / b
    except ValueError:
        print("Enter valid integers")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print("Result:", result)
    finally:
        print("Division operation completed")
def check_age():
    try:
        age = int(input("Enter age: "))
        if age < 18:
            raise ValueError("Age must be 18 or above")
        print("Eligible")
    except ValueError as e:
        print(e)
def withdraw():
    try:
        balance = 5000
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > balance:
            raise InsufficientBalanceError("Insufficient balance")
        print("Remaining balance:", balance - amount)
    except (ValueError, InsufficientBalanceError) as e:
        print(e)
    finally:
        print("Transaction completed")
class InsufficientBalanceError(Exception): pass
while True:
    print("\n1. Divide\n2. Check Age\n3. Withdraw\n4. Exit")
    try:
        choice = int(input("Enter choice: "))
        if choice == 1:
            divide()
        elif choice == 2:
            check_age()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            print("Goodbye")
            break
        else:
            raise InvalidChoiceError("Invalid menu choice")
    except ValueError:
        print("Please enter a number")
    except InvalidChoiceError as e:
        print(e)