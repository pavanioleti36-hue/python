pswd= input("enter password: ")
dig= False
for x in pswd:
    if x.isdigit():
        dig= True
if dig:
    print("Yes ! password has a digit")
else:
    print("No ! password has a no digit")
