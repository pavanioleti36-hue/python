uname = input("Enter username: ")
usernames = ["pavani", "swarupa", "prasanna", "divya"]
if uname.lower() in usernames:
    print("Username exists in the list")
else:
    print("Username does not exist in the list")