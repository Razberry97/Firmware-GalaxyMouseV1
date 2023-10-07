class baseHandler:
    def __init__(self):
        self.mouse = None
        self.keyboard = None

    def setMouse(self, mouse):
        self.mouse = mouse
    
    def setKeyboard(self, keyboard):
        self.keyboard = keyboard