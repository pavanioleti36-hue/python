def largest_smallest(numbers):
    if not numbers:
        return "List is empty"
    largest = smallest = numbers[0]
    for n in numbers:
        if n > largest:
            largest = n
        if n < smallest:
            smallest = n
    return largest, smallest
print(largest_smallest([10, 5, 30, 2, 20]))