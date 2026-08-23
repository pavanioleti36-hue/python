vegetables= [("tomatos", 20, 5),
             ("brinjal", 15, 3),
             ("potatos", 30, 6),
             ("carrots", 50, 2)]
print("vegetables total price: ")
for veg, pri, qua in vegetables:
    print("->item :",veg, " ->Total price: ",pri*qua)