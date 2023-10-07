from handlers.basePressButton import basePressButton

class singlePressGrid(basePressButton):
    def __init__(self, buttonToPress, buttonX, buttonY):
        super().__init__(buttonToPress)
        self.isPressed = False
        self.buttonX = buttonX
        self.buttonY = buttonY

    def handle(self, dic):
        if dic[self.buttonX] == 0 or dic[self.buttonY] == 0:
            self.isPressed = False
            return
        if not self.isPressed:
            self.pressAll(self.keyboard)
            self.releaseAll(self.keyboard)
            self.isPressed = True
