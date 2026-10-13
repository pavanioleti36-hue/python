def average(numbers):
    if not numbers:
        return "List is empty"
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)
print(average([10, 20, 30, 40]))