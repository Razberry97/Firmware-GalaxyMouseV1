from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller as MouseController

class baseHandler:
    def __init__(self):
        self.mouse: MouseController = None
        self.keyboard: Controller = None

    def setMouse(self, mouse: MouseController):
        self.mouse = mouse
    
    def setKeyboard(self, keyboard: Controller):
        self.keyboard = keyboard