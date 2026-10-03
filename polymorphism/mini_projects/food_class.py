class Pizza:
    def calculate_price(self):
        return 250
class Burger:
    def calculate_price(self):
        return 150
class Biryani:
    def calculate_price(self):
        return 200
class Sandwich:
    def calculate_price(self):
        return 120
foods = [Pizza(), Burger(), Biryani(), Sandwich()]
total = 0
for food in foods:
    price = food.calculate_price()
    print("Price:", price)
    total += price
print("Total Price:", total)