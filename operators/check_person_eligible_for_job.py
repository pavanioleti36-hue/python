age= int(input("Enter your age: "))
qualification= input("Enter your qualification: ")
if age >= 18 and qualification.lower() == "graduate":
    print("You are eligible for the job")
else:
    print("You are not eligible for the job")