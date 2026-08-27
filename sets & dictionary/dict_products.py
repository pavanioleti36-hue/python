products = {
    "Apples": 15,
    "Bananas": 8,
    "Oranges": 12,
    "Mangoes": 5,
    "Grapes": 20
}
print("Products with quantity less than 10:")
for item, qty in products.items():
    if qty < 10:
        print(item + " - " + str(qty))