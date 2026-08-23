lis= [50, 30 ,80, 10, 30, 20,30,60,40, 20, 70]
newlist= []
for x in lis:
    if x not in newlist:
        newlist.append(x)
print("old list: ",lis)        
print("new list: ",newlist)        