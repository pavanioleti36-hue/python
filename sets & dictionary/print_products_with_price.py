products = {
    "Smartphone": 25000,
    "Charger": 800,
    "Tablet": 15000,
    "Smartwatch": 4500,
    "Speaker": 950
}
for item, price in products.items():
    if price > 1000:
        print(item + " - " + str(price))