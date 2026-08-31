apple_price = int(input("enter apple price:"))
banana_price = int(input("enter banana price:"))
milk_price = int(input("enter milk price:"))
apple_qty = 2
banana_qty = 6
milk_qty = 1
bill = 0
bill += apple_price * apple_qty
bill += banana_price * banana_qty
bill += milk_price * milk_qty

print("Total Shopping Bill: " + str(bill))