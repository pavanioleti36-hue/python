password = input("Enter password: ")
try:
    if len(password) < 8:
        raise ValueError("Password must contain at least 8 characters")
    print("Valid password")
except ValueError as e:
    print(e)