def search_key(data, key):
    try:
        print("Value:", data[key])
    except KeyError:
        print("Key not found")
search_key({"name": "Ravi", "age": 20}, "city")