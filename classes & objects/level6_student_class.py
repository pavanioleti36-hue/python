class Number:
    def __init__(self, value):
        self.value = value

    def is_even(self):
        return self.value % 2 == 0

    def is_odd(self):
        return self.value % 2 != 0

    def is_prime(self):
        if self.value < 2:
            return False
        for i in range(2, int(self.value ** 0.5) + 1):
            if self.value % i == 0:
                return False
        return True

    def is_palindrome(self):
        return str(self.value) == str(self.value)[::-1]


# Example usage
num1 = Number(121)
num2 = Number(17)

print("121 is even:", str(num1.is_even()))
print("121 is odd:", str(num1.is_odd()))
print("121 is prime:", str(num1.is_prime()))
print("121 is palindrome:", str(num1.is_palindrome()))

print("17 is even:", str(num2.is_even()))
print("17 is odd:", str(num2.is_odd()))
print("17 is prime:", str(num2.is_prime()))
print("17 is palindrome:", str(num2.is_palindrome()))
