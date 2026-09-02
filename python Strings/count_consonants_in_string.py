str= "pavanioleti"
count=0
for x in str:
    if x not  in "aeiouAEIOU":
        count+=1
print("the string is :",str)
print("this string has ",count,"consonants")  