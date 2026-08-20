class Temperature:
    def __init__(self, value):
        self.value = value

    def celsius_to_fahrenheit(self):
        return (self.value * 9/5) + 32

    def fahrenheit_to_celsius(self):
        return (self.value - 32) * 5/9


# Example usage
temp1 = Temperature(37)
print("37°C in Fahrenheit: " + str(temp1.celsius_to_fahrenheit()))

temp2 = Temperature(98.6)
print("98.6°F in Celsius: " + str(temp2.fahrenheit_to_celsius()))
