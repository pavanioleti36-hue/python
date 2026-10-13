def count_even_odd(numbers):
    even = sum(1 for n in numbers if n % 2 == 0)
    odd = sum(1 for n in numbers if n % 2 != 0)
    return {"even": even, "odd": odd}
print(count_even_odd([1, 2, 3, 4, 5, 6]))