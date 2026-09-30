class  onlinecourse:
    def start(self):
        print("online course starting")
class offlinecourse:
    def start(self):
        print("offline course starting")
def obj_cls(obj):
    obj.start()
online= onlinecourse()
offline= offlinecourse()
obj_cls(online)
obj_cls(offline)                    