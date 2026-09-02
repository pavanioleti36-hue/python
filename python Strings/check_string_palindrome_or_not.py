str= input("enter a string:")
res= ""
for x in str:
    if x not in " ":
        res = x+res 
if str== res:
    print("it is a palindrome")
else:
    print("not a palindrome")    