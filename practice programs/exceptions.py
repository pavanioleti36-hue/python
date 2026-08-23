<<<<<<< HEAD
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age >= 18:
        print("Eligible to vote.")
    else:
        print("Not eligible to vote.")
except ValueError as e:
=======
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age >= 18:
        print("Eligible to vote.")
    else:
        print("Not eligible to vote.")
except ValueError as e:
>>>>>>> cc9c058bde5fd6ced8fb6651372cb99cdb3da7a2
    print("Invalid input:", e)