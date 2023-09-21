class singlePressButton:
    def __init__(self, buttonToPress, buttonName):
        self.isPressed = False
        self.buttonToPress = buttonToPress
        self.buttonName = buttonName

    def handle(self, dic, keyboard):
        if dic[self.buttonName] == 0:
            self.isPressed = False
            return
        if not self.isPressed:
            if type(self.buttonToPress) == list:
                for but in self.buttonToPress:
                    keyboard.press(but)
            else:
                keyboard.press(self.buttonToPress)
            self.isPressed = True