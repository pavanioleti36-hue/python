try:
    a= int(input("enter a value:"))
    b= int(input("enter b value:"))
    c= a+b
except ValueError:
    print("invalid numeric input")