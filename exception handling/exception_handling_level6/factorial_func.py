def factorial(n):
    try:
        if n < 0:
            raise ValueError("Number cannot be negative")
        result = 1
        for i in range(1, n + 1):
            result *= i
        print("Factorial:", result)
    except (ValueError, TypeError) as e:
        print("Invalid input:", e)
factorial(5)