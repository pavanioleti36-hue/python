class food:
    def deliver(self):
        print("Food delivered")
class things:
    def deliver(self):
        print("Things delivered")
class clothes:
    def deliver(self):
        print("Clothes delivered")
def assign_deliver(employee):
    employee.deliver()
food_item = food()
things_item = things()
clothes_item = clothes()
assign_deliver(food_item)
assign_deliver(things_item)
assign_deliver(clothes_item)