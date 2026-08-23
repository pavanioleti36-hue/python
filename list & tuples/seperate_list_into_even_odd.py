lis= [22, 7, 14, 3, 16, 5, 29, 28,54, 99,14, 6]
even= []
odd= []
for x in lis:
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
print("even numbers list : ",even)   
print("odd numbers list : ",odd)                     