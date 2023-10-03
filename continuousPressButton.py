class continuousPressButton:
    def __init__(self, buttonToPress, buttonName):
        self.isPressed = False
        self.buttonToPress = buttonToPress
        self.buttonName = buttonName

    def handle(self, dic, keyboard):
        if dic[self.buttonName] == 0:
            if self.isPressed:
                self.releaseAll(keyboard)
                self.isPressed = False
        else: 
            if not self.isPressed:
                self.pressAll(keyboard)
                self.isPressed = True
    
    def pressAll(self, keyboard):
        if type(self.buttonToPress) == list:
            for but in self.buttonToPress:
                keyboard.press(but)
        else:
            keyboard.press(self.buttonToPress)

    def releaseAll(self, keyboard):
        if type(self.buttonToPress) == list:
            for but in self.buttonToPress:
                keyboard.release(but)
        else:
            keyboard.release(self.buttonToPress)