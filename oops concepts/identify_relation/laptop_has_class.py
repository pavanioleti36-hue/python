class Keyboard:
    def type_text(self):
        print("Typing...")
class Laptop:
    def __init__(self):
        self.keyboard = Keyboard()
    def use_keyboard(self):
        self.keyboard.type_text()
laptop = Laptop()
laptop.use_keyboard()