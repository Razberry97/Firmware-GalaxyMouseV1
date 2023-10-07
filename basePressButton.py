class basePressButton:
    def __init__(self, buttonToPress):
        self.buttonToPress = buttonToPress

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