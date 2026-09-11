product_price= float(input("Enter the price of the product: "))
product_quantity= int(input("Enter the quantity of the product: "))

total_price= product_price * product_quantity
if (total_price >= 1000) and (total_price <= 50000):
    discount= total_price * 0.32
    discounted_price= total_price - discount
    print("The discounted price of the product is: ", discounted_price)
print("original price of the product is: ", total_price)