product_price = float(input("Enter product price: "))
discount_percentage = float(input("Enter discount percentage: "))
discount_amount = product_price * (discount_percentage / 100)
final_price = product_price - discount_amount
print("Final price =", final_price)