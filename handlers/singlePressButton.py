from handlers.basePressButton import basePressButton

class singlePressButton(basePressButton):
    def __init__(self, buttonToPress, buttonName):
        super().__init__(buttonToPress)
        self.isPressed = False
        self.buttonName = buttonName

    def handle(self, dic, keyboard):
        if dic[self.buttonName] == 0:
            self.isPressed = False
            return
        if not self.isPressed:
            self.pressAll(keyboard)
            self.releaseAll(keyboard)
            self.isPressed = True