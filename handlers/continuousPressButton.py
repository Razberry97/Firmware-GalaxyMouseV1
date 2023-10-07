from handlers.basePressButton import basePressButton

class continuousPressButton(basePressButton):
    def __init__(self, buttonToPress, buttonName):
        super().__init__(buttonToPress)
        self.isPressed = False
        self.buttonName = buttonName

    def handle(self, dic):
        if dic[self.buttonName] == 0:
            if self.isPressed:
                self.releaseAll(self.keyboard)
                self.isPressed = False
        else: 
            if not self.isPressed:
                self.pressAll(self.keyboard)
                self.isPressed = True
    