class InvalidPasswordError(Exception):
    pass
def validate_password(password):
    if len(password) < 8:
        raise InvalidPasswordError("Password must contain at least 8 characters")
    print("Valid password")
try:
    validate_password("abc")
except InvalidPasswordError as e:
    print(e)