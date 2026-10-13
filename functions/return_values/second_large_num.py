def second_largest(numbers):
    unique = list(set(numbers))
    if len(unique) < 2:
        return "No second-largest number"
    unique.sort()
    return unique[-2]
print(second_largest([10, 20, 40, 30, 40]))