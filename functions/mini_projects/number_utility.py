def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
def is_palindrome(n):
    return str(n) == str(n)[::-1]
def factorial(n):
    if n < 0:
        return "Invalid number"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result
def even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"
def is_armstrong(n):
    digits = str(n)
    return n >= 0 and sum(int(d) ** len(digits) for d in digits) == n
while True:
    print("\n1.Prime 2.Palindrome 3.Factorial 4.Fibonacci 5.Even/Odd 6.Armstrong 7.Exit")
    choice = input("Enter choice: ")
    if choice == "7":
        break
    if choice in ["1", "2", "3", "5", "6"]:
        n = int(input("Enter number: "))
        functions = {"1": is_prime, "2": is_palindrome, "3": factorial, "5": even_odd, "6": is_armstrong}
        print(functions[choice](n))
    elif choice == "4":
        n = int(input("Enter number of terms: "))
        print(fibonacci(n) if n >= 0 else "Enter a non-negative number")
    else:
        print("Invalid choice")