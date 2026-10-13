def separate_numbers(*args):
    even = []
    odd = []
    for n in args:
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)
    return even, odd
print(separate_numbers(1, 2, 3, 4, 5, 6, 7, 8))