lis= [2, 8, 316, 4,5,3,67,13,25,3,66]
small=lis[0]
for x in lis:
    if x< small:
        small= x
print("values in list: ",lis)
print("largest value in list: ",small) 