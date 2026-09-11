age= int(input("Enter your age: "))
membership= input("Enter your membership type (Gold/Silver/Bronze): ")
if (age >= 25 and age<=60) or membership.lower() == "gold":
    print("You are eligible for  discount")
else:
    print("You are not eligible for discount")