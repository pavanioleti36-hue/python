def largest(numbers):
    if not numbers:
        return "List is empty"
    result = numbers[0]
    for n in numbers:
        if n > result:
            result = n
    return result
print(largest([10, 50, 30, 20]))