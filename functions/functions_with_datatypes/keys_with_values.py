def get_keys(data):
    return [key for key, value in data.items() if value > 50]
print(get_keys({"A": 60, "B": 40, "C": 80}))