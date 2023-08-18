class singlePressButton:
    def __init__(self, buttonToPress, buttonName, keyboard):
        self.isPressed = False
        self.buttonToPress = buttonToPress
        self.buttonName = buttonName
        self.keyboard = keyboard

    def handle(self, dic):
        if dic[self.buttonName] == 0:
            self.isPressed = False
            return
        if not self.isPressed:
            if type(self.buttonToPress) == list:
                for but in self.buttonToPress:
                    self.keyboard.press(but)
            else:
                self.keyboard.press(self.buttonToPress)
            self.isPressed = True