cart = {}
def add_product():
    name = input("Enter product: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    if price >= 0 and quantity > 0:
        cart[name] = cart.get(name, [price, 0])
        cart[name][1] += quantity
        cart[name][0] = price
    else:
        print("Invalid price or quantity")
def remove_product():
    name = input("Enter product: ")
    print("Removed" if cart.pop(name, None) is not None else "Product not found")
def display_cart():
    for name, item in cart.items():
        print(name, "Price:", item[0], "Quantity:", item[1])
def calculate_total():
    return sum(price * quantity for price, quantity in cart.values())
def checkout():
    display_cart()
    print("Total:", calculate_total())
    cart.clear()
while True:
    print("\n1.Add 2.Remove 3.Display 4.Total 5.Checkout 6.Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_product()
    elif choice == "2":
        remove_product()
    elif choice == "3":
        display_cart()
    elif choice == "4":
        print("Total:", calculate_total())
    elif choice == "5":
        checkout()
    elif choice == "6":
        break
    else:
        print("Invalid choice")