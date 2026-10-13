def profile(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
profile(name="Anu", age=21, city="Hyderabad", profession="Student")