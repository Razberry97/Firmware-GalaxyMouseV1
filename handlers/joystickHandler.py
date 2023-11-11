import win32api
import datetime
import math
from pynput.keyboard import Key
from pynput.mouse import Button
from handlers.baseHandler import baseHandler
from enum import Enum
from ctypes import windll


class JOYSTICK_STATE(Enum):
    NON_PREMUTO = 0
    PRESSING = 1
    RELEASING = 2


class JoyStickHandler(baseHandler):
    def __init__(self):
        super().__init__()
        self.joyState = JOYSTICK_STATE.NON_PREMUTO
        self.timeToRelease = None
        self.radius = 300
        self.sensitivity = 0.5
        self.centerX = 1000
        self.centerY = 500

    def deadzoning(self, val):
        if abs(val) < 10:
            return 0
        return val

    def coordinatePipeline(self, val):
        val = self.deadzoning(val)
        val /= 100
        return val

    def pressKeys(self):
        self.keyboard.press(Key.shift)
        self.mouse.press(Button.middle)
        self.keyboard.press(Key.ctrl_l)

    def releaseKeys(self):
        self.keyboard.release(Key.shift)
        self.mouse.release(Button.middle)
        self.keyboard.release(Key.ctrl_l)

    def distance(self, x1, y1, x2, y2):
        return math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2)

    def handleMouseMovement(self, xVal, yVal):
        xmPos, ymPos = win32api.GetCursorPos()
        win32api.ShowCursor(False)

        if (self.distance(xmPos, ymPos, self.centerX, self.centerY) > self.radius):
            xmPos = self.centerX
            ymPos = self.centerY
            self.releaseKeys()
            win32api.SetCursorPos((self.centerX, self.centerY))
            self.mouse.move(int(xVal), int(yVal))
            self.pressKeys()
        else:
            self.mouse.move(int(xVal), int(yVal))

    def handle(self, dic):
        xVal = dic['XValue']
        yVal = dic['YValue']

        xVal = self.coordinatePipeline(xVal)
        yVal = self.coordinatePipeline(yVal)

        if self.joyState == JOYSTICK_STATE.NON_PREMUTO:
            if yVal != 0 or xVal != 0:
                self.joyState = JOYSTICK_STATE.PRESSING
                # disable real mouse
                windll.user32.BlockInput(True)

                self.pressKeys()
                self.handleMouseMovement(xVal, yVal)
        elif self.joyState == JOYSTICK_STATE.PRESSING:
            if yVal == 0 and xVal == 0:
                self.timeToRelease = (
                    datetime.datetime.now() +
                    datetime.timedelta(seconds=0.1)
                )
                self.joyState = JOYSTICK_STATE.RELEASING
            self.handleMouseMovement(xVal, yVal)
        elif self.joyState == JOYSTICK_STATE.RELEASING:
            self.handleMouseMovement(xVal, yVal)
            if yVal != 0 or xVal != 0:
                self.joyState = JOYSTICK_STATE.PRESSING
            else:
                currentTime = datetime.datetime.now()
                if (
                        self.timeToRelease is not None and
                        self.timeToRelease < currentTime
                ):
                    self.releaseKeys()
                    self.timeToRelease = None
                    self.joyState = JOYSTICK_STATE.NON_PREMUTO
                    windll.user32.BlockInput(False)
                    win32api.SetCursorPos((self.centerX, self.centerY))
