import win32api
import datetime
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller as MouseController

from handlers.baseHandler import baseHandler

class JoyStickHandler(baseHandler):
    def __init__(self):
        super().__init__()
        self.isPressing = False
        self.timeToRelease = None
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
        if self.timeToRelease == None:
            self.keyboard.press(Key.shift)
            self.mouse.press(Button.middle)
            self.keyboard.press(Key.ctrl_l)
        else:
            self.timeToRelease = None
        self.isPressing = True

    def releaseKeys(self):
        self.timeToRelease = datetime.datetime.now() + datetime.timedelta(seconds=2)
        self.isPressing = False

    def handleMouseMovement(self, xVal, yVal, doPacman):
        squareX = 1000
        squareY = 500
        xmPos,ymPos = win32api.GetCursorPos()
        win32api.ShowCursor(False)

        if (not doPacman and (xmPos < squareX - self.squareLato or xmPos > squareX + self.squareLato or 
            ymPos < squareY - self.squareLato or ymPos > squareY + self.squareLato)):
            xmPos = squareX
            ymPos = squareY
            self.releaseKeys()
            win32api.SetCursorPos((xmPos - int(xVal), ymPos + int(yVal)))
            self.pressKeys()
        else:
            win32api.SetCursorPos((xmPos - int(xVal), ymPos + int(yVal)))


    def handle(self, dic):
        xVal = dic['XValue']
        yVal = dic['YValue']

        xVal = self.coordinatePipeline(xVal)
        yVal = self.coordinatePipeline(yVal)
        if yVal != 0 or xVal != 0:

            if self.isPressing == False:
                self.pressKeys()
            

            self.handleMouseMovement(xVal, yVal, False)

        elif self.isPressing:
            self.releaseKeys()

        currentTime = datetime.datetime.now()
        if self.timeToRelease != None and self.timeToRelease > currentTime:
            self.mouse.release(Button.middle)
            self.timeToRelease = None

