user_name= "Pavani"
user_password= "pavani123!"
uname= input("Enter username: ")
pswd= input("Enter password: ")
if (uname==user_name) and (pswd==user_password):
    print("Login successful")
elif (uname==user_name) and (pswd!=user_password):
    print("Invalid password")
elif (uname!=user_name) and (pswd==user_password):
    print("Invalid username")
else:
    print("Invalid username and password")        