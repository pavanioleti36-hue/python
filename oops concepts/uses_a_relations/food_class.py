class DeliveryService:
    def deliver(self, address):
        print("Food delivered to:", address)


class FoodOrder:
    def __init__(self, food, address):
        self.food = food
        self.address = address

    def place_order(self, delivery_service):
        print("Food Ordered:", self.food)
        delivery_service.deliver(self.address)


order = FoodOrder("Pizza", "Hyderabad")
delivery = DeliveryService()

order.place_order(delivery)