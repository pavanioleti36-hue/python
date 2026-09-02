name = input("Enter student name: ").strip().title()
course = input("Enter course: ").strip().title()
mobile = input("Enter mobile number: ").strip()
if not name.replace(" ", "").isalpha():
     print("Invalid student name")
elif not mobile.isdigit() or len(mobile) != 10:
     print("Invalid mobile number")
else:
     print("\nRegistration Successful")
print(f"Name   : {name}")
print(f"Course : {course}")
print(f"Mobile : {mobile}")

#login page
saved_uname = "admin"
saved_pswd = "Python@123"
username = input("Enter username: ").strip()
pswd = input("Enter password: ")
if username == saved_uname and pswd == saved_pswd:
     print("Login Successful")
else:
     print("Invalid Username or Password")