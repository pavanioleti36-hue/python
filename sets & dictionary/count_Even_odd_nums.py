dict= {1,2,3,4,5,6,7,8,9,0}
even= 0
odd= 0
for x in dict:
    if x%2==0:
        even +=1
    else:
        odd +=1
print("dictionary :",dict)
print("even numbers count :",even)
print("odd numbers count :",odd)            