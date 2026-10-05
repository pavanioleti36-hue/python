class Room:
    def __init__(self, name):
        self.name = name
    def display(self):
        print("Room:", self.name)
class House:
    def __init__(self):
        self.rooms = [
            Room("Bedroom"),
            Room("Kitchen"),
            Room("Hall")
        ]
    def show_rooms(self):
        for room in self.rooms:
            room.display()
h = House()
h.show_rooms()