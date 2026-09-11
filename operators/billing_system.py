item1 = int(input("Enter price of Item 1: "))
item2 = int(input("Enter price of Item 2: "))
item3 = int(input("Enter price of Item 3: "))
quantity = int(input("Enter quantity for each item: "))
total = (item1 + item2 + item3) * quantity
bill = 0
bill += item1 * quantity
bill += item2 * quantity
bill += item3 * quantity

high_value_order = total >= 1000   

if high_value_order:
    discount = 0.10   
else:
    discount = 0.0  
final_amount = bill - (bill * discount)

print("Total Bill:", bill)
print("Discount Applied:", discount * 100, "%")
print("Final Amount to Pay:", final_amount)