lis= [1,2,3,4,5,6,7,8,9]
newlist= []
sq= 0
for x in lis:
    if x !=0:
        sq= x*x
    newlist.append(sq)
print("normal list: ",lis)    
print("square list: ",newlist)    