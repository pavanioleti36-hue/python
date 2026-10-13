class InvalidPasswordError(Exception):
    pass
try:
    password = input("Enter password: ")
    if len(password) < 8:
        raise InvalidPasswordError("Password must contain at least 8 characters")
    print("Valid password")
except InvalidPasswordError as e:
    print(e)