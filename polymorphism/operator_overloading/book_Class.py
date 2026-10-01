class Book:
    def __init__(self, price):
        self.price = price

    def __gt__(self, other):
        return self.price > other.price
b1 = Book(500)
b2 = Book(300)
print(b1 > b2)