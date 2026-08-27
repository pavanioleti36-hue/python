products = {
    "Laptop": 55000,
    "Mouse": 750,
    "Keyboard": 1200,
    "Monitor": 8500,
    "Headphones": 999
}
expensive_products = {item for item, price in products.items() if price > 5000}
print("Products above ₹5,000:")
for product in expensive_products:
    print(product)