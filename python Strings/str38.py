email= input("enter email:-")
if "@" in email and "." in email:
    print("valid email")
else:
    print("inavlid email address")    

#mobile number validation
mobile = input("Enter mobile number: ")
if mobile.isdigit() and len(mobile) == 10:
     print("Valid Mobile Number")
else:
     print("Invalid Mobile Number")

#name valudation
name = input("Enter your name: ").strip()
if name.replace(" ", "").isalpha():
    print("Valid Name")
else:
    print("Name should contain letters only")    