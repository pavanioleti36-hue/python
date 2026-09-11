username = input("Enter username: ")
password = input("Enter password: ")
email = input("Enter email: ")
username_ok = len(username) >= 5
password_ok = len(password) >= 8
email_ok = "@" in email and "." in email
if username_ok and password_ok and email_ok:
    print("Registration Successful!")
else:
    print("Registration Failed!")
    if not username_ok:
        print("Username must be at least 5 characters long.")
    if not password_ok:
        print("Password must be at least 8 characters long.")
    if not email_ok:
        print("Email must contain '@' and '.'")