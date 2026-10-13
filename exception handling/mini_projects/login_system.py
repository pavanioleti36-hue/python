class InvalidUsernameError(Exception): pass
class WeakPasswordError(Exception): pass
class DuplicateUsernameError(Exception): pass
class InvalidLoginError(Exception): pass
class LoginSystem:
    def __init__(self):
        self.users = {}
    def register(self, username, password):
        try:
            if not username.strip():
                raise InvalidUsernameError("Username cannot be empty")
            if username in self.users:
                raise DuplicateUsernameError("Username already exists")
            if len(password) < 8:
                raise WeakPasswordError("Password must contain at least 8 characters")
            self.users[username] = password
            print("Registration successful")
        except (InvalidUsernameError, WeakPasswordError, DuplicateUsernameError) as e:
            print(e)
    def login(self, username, password):
        try:
            if self.users.get(username) != password:
                raise InvalidLoginError("Invalid username or password")
            print("Login successful")
        except InvalidLoginError as e:
            print(e)
system = LoginSystem()
system.register("student", "python123")
system.register("student", "welcome123")
system.login("student", "python123")