class InvalidUsernameError(Exception):
    pass
class InvalidPasswordError(Exception):
    pass
class LoginSystem:
    def login(self, username, password):
        try:
            if username != "admin":
                raise InvalidUsernameError("Invalid username")
            if password != "python123":
                raise InvalidPasswordError("Invalid password")
            print("Login successful")
        except (InvalidUsernameError, InvalidPasswordError) as e:
            print(e)
login = LoginSystem()
login.login("user", "12345")