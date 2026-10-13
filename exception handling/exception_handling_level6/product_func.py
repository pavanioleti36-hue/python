def calculate_price(price, quantity):
    try:
        if price < 0 or quantity <= 0:
            raise ValueError("Invalid price or quantity")
        print("Total price:", price * quantity)
    except (ValueError, TypeError) as e:
        print(e)
calculate_price(100, 3)