def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    sequence = fibonacci(n - 1)
    next_number = 0 if len(sequence) < 2 else sequence[-1] + sequence[-2]
    if len(sequence) == 1:
        next_number = 1
    sequence.append(next_number)
    return sequence
print(fibonacci(7))