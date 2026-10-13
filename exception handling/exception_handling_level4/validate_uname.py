username = input("Enter username: ")
try:
    if not username.strip():
        raise ValueError("Username cannot be empty")
    print("Username:", username)
except ValueError as e:
    print(e)