str= "pavani#16"
count=0
for x in str:
    if x in "1234567890":
        count+=1
print("the string is :",str)
print("this string has ",count,"digits")  