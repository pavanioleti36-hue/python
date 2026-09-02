str= "pavani is a good girl"
count=0
for x in str:
    if x in " ":
        count+=1
print("the string is :",str)
print("this string has ",count,"spaces")  