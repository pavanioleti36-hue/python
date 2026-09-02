str= "manoj"
res= ""
for x in str:
    if x not in " ":
        res = x+res
print("the string after reverse:",res)        