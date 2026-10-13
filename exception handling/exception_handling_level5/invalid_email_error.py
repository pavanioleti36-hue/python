class InvalidEmailError(Exception):
    pass
try:
    email = input("Enter email: ")
    if "@" not in email or "." not in email.split("@")[-1]:
        raise InvalidEmailError("Invalid email address")
    print("Valid email")
except InvalidEmailError as e:
    print(e)