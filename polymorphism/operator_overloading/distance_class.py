class Distance:
    def __init__(self, km):
        self.km = km
    def __add__(self, other):
        return Distance(self.km + other.km)
d1 = Distance(10)
d2 = Distance(15)
d3 = d1 + d2
print("Total Distance:", d3.km, "km")