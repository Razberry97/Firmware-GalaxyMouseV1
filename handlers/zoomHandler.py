class ZoomHandler:
    def __init__(self, mouse, keyboard):
        self.mouse = mouse
        self.keyboard = keyboard
        self.button6Modular = 0
        self.button7Modular = 0

    def handle(self, dic, _keyboard):
        
        button6 = dic['button6']

        if button6 == 1:
            self.button6Modular = self.button6Modular + 1
            if self.button6Modular % 6 == 0:
                self.mouse.scroll(1,0)
        
        button7 = dic['button7']

        if button7 == 1:
            self.button7Modular = self.button7Modular + 1
            if self.button7Modular % 6 == 0:
                self.mouse.scroll(-1,0)