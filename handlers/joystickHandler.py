import win32api
import datetime
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller as MouseController

class JoyStickHandler:
    def __init__(self, mouse, keyboard):
        self.mouse = mouse
        self.keyboard = keyboard
        self.isPressing = False
        self.lastPress = None
        self.squareLato = 100

    def deadzoning(self, val):
        if abs(val) < 10:
            return 0
        return val

    def coordinatePipeline(self, val):
        val = self.deadzoning(val)
        val /= 100
        return val

    def pressKeys(self):
        currentTime = datetime.datetime.now()
        if self.lastPress != None:
            delta = self.lastPress - currentTime
            if delta.microseconds < 550000:
                return
        self.keyboard.press(Key.shift)
        self.mouse.press(Button.middle)
        self.keyboard.press(Key.ctrl_l)
        self.isPressing = True

    def releaseKeys(self):
        self.keyboard.release(Key.shift)
        self.mouse.release(Button.middle)
        self.keyboard.release(Key.ctrl_l)
        self.lastPress = datetime.datetime.now()
        self.isPressing = False


    def handle(self, dic, _keyboard):
        xVal = dic['XValue']
        yVal = dic['YValue']

        xVal = self.coordinatePipeline(xVal)
        yVal = self.coordinatePipeline(yVal)

        if yVal != 0 or xVal != 0:

            if self.isPressing == False:
                self.pressKeys()

            xmPos,ymPos = win32api.GetCursorPos()

            if (xmPos < 1000 - self.squareLato or xmPos > 1000 + self.squareLato or 
                ymPos < 500 - self.squareLato or ymPos > 500 + self.squareLato):
                xmPos = 1000
                ymPos = 500
                self.releaseKeys()
                win32api.SetCursorPos((xmPos - int(xVal), ymPos + int(yVal)))
                self.pressKeys()
            else:
                win32api.SetCursorPos((xmPos - int(xVal), ymPos + int(yVal)))

        elif self.isPressing:
            self.releaseKeys()

