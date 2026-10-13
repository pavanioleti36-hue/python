def outer():
    def inner():
        print("Welcome, Pavani!")
    return inner
func = outer()
func()