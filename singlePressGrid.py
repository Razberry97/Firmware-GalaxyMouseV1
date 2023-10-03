class singlePressGrid:
    def __init__(self, buttonToPress, buttonX, buttonY):
        self.isPressed = False
        self.buttonToPress = buttonToPress
        self.buttonX = buttonX
        self.buttonY = buttonY

    def handle(self, dic, keyboard):
        if dic[self.buttonX] == 0 or dic[self.buttonY] == 0:
            self.isPressed = False
            return
        if not self.isPressed:
            if type(self.buttonToPress) == list:
                for but in self.buttonToPress:
                    keyboard.press(but)
                    keyboard.release(but)
            else:
                keyboard.press(self.buttonToPress)
                keyboard.release(self.buttonToPress)
            self.isPressed = True