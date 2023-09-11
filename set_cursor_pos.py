import win32api
import datetime
import serial
import json
import time
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller as MouseController

from singlePressButton import singlePressButton

settings = json.load(open("C:\\Users\\scorp\\Desktop\\things\\3d mouse firmware\\settings.json"))


keyboard = Controller()
mouse = MouseController()


def deadzoning(val):
    if abs(val) < 10:
        return 0
    return val

def coordinatePipeline(val):
    val = deadzoning(val)
    val /= 100
    return val

i = 0

squareLato = 100

isPressing = False

lastPress = None

def pressKeys():
    global lastPress
    global isPressing
    currentTime = datetime.datetime.now()
    if lastPress != None:
        delta = lastPress - currentTime
        if delta.microseconds < 600:
            return
    keyboard.press(Key.shift)
    mouse.press(Button.middle)
    keyboard.press(Key.ctrl_l)
    isPressing = True

def releaseKeys():
    global lastPress
    global isPressing
    keyboard.release(Key.shift)
    mouse.release(Button.middle)
    keyboard.release(Key.ctrl_l)
    lastPress = datetime.datetime.now()
    isPressing = False


button6Modular = 0
button7Modular = 0

buttonList = [
    singlePressButton('a', 'joyButt'),
    singlePressButton(Key.esc, 'button1'),
    singlePressButton(['a', 'b'], 'button2'),
]

toInit = True

while True:
    try:
        if toInit:
            ser = serial.Serial(settings["ARDUINO_PORT"], 9600)
            toInit = False

        line = ser.readline().decode('utf-8')
        dic = json.loads(line)

        xVal = dic['XValue']
        yVal = dic['YValue']

        xVal = coordinatePipeline(xVal)
        yVal = coordinatePipeline(yVal)

        if yVal != 0 or xVal != 0:

            if isPressing == False:
                pressKeys()

            xmPos,ymPos = win32api.GetCursorPos()

            if (xmPos < 1000 - squareLato or xmPos > 1000 + squareLato or 
                ymPos < 500 - squareLato or ymPos > 500 + squareLato):
                xmPos = 1000
                ymPos = 500
                releaseKeys()
                win32api.SetCursorPos((xmPos - int(xVal), ymPos + int(yVal)))
                pressKeys()
            else:
                win32api.SetCursorPos((xmPos - int(xVal), ymPos + int(yVal)))

        elif isPressing:
            releaseKeys()

        button6 = dic['button6']

        if button6 == 1:
            button6Modular = button6Modular + 1
            if button6Modular % 6 == 0:
                mouse.scroll(1,0)
        
        button7 = dic['button7']

        if button7 == 1:
            button7Modular = button7Modular + 1
            if button7Modular % 6 == 0:
                mouse.scroll(-1,0)
        
        for buttonHandler in buttonList:
            buttonHandler.handle(dic, keyboard)
    except KeyboardInterrupt:
        exit()
    except Exception as e:
        print(str(e))
        time.sleep(1)
        toInit = True