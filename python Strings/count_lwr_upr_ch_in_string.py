str= "Pavani is a GOOD GIRL"
lwr=0
upr=0
sp=0
for x in str:
    if x.islower():
        lwr+=1
    elif x.isupper():
        upr+=1
    else:
        sp+=1             
print("the string is :",str)
print("this string has ",lwr,"lower characters")  
print("this string has ",upr,"upper characters")  