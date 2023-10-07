import win32api
import datetime
import serial
import json
import time
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller as MouseController
from singlePressGrid import singlePressGrid
from continuousPressButton import continuousPressButton
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
        if delta.microseconds < 550000:
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
    singlePressButton    (Key.shift,     'joyButt'),             
    singlePressGrid      (Key.esc,       'gridX6' , 'gridY1'),           #pinky
    continuousPressButton(Key.shift,     'gridX6' , 'gridY2'),           #ring
    continuousPressButton(Key.ctrl,      'gridX6' , 'gridY3'),           #middle
    singlePressGrid      (['x'],         'gridX6' , 'gridY4'),           #index
    singlePressGrid      (['s'],         'gridX6' , 'gridY5'),           #thumb

    singlePressGrid      ([Key.ctrl, 'c'],  'gridX1' , 'gridY1'),     
    singlePressGrid      ([Key.ctrl, 'v'],  'gridX2' , 'gridY1'),     
    singlePressGrid      (['-'],            'gridX3' , 'gridY1'),
    singlePressGrid      (['+'],            'gridX4' , 'gridY1'),    
    singlePressGrid      (Key.backspace,    'gridX5' , 'gridY1'),    
    singlePressGrid      ([Key.ctrl, Key.left, Key.shift, Key.right], 'gridX1' , 'gridY2'),   #select entire word 
    singlePressGrid      (['1'],            'gridX2' , 'gridY2'),
    singlePressGrid      (['2'],            'gridX3' , 'gridY2'),
    singlePressGrid      (['3'],            'gridX4' , 'gridY2'),
    singlePressGrid      ([Key.ctrl, Key.right],  'gridX5' , 'gridY2'),   #go to end of the line 
    singlePressGrid      (['/'],            'gridX1' , 'gridY3'),
    singlePressGrid      (['4'],            'gridX2' , 'gridY3'),
    singlePressGrid      (['5'],            'gridX3' , 'gridY3'),
    singlePressGrid      (['6'],            'gridX4' , 'gridY3'),
    singlePressGrid      ([Key.ctrl, Key.left],   'gridX5' , 'gridY3'),   #go to start of the line  
    singlePressGrid      (['*'],            'gridX1' , 'gridY4'),
    singlePressGrid      (['7'],            'gridX2' , 'gridY4'),
    singlePressGrid      (['8'],            'gridX3' , 'gridY4'),
    singlePressGrid      (['9'],            'gridX4' , 'gridY4'),
    singlePressGrid      (Key.enter,        'gridX5' , 'gridY4'),        
    singlePressGrid      (['.'],            'gridX1' , 'gridY5'),
    singlePressGrid      (['0'],            'gridX2' , 'gridY5'),
    singlePressGrid      ([''],             'gridX3' , 'gridY5'),
    singlePressGrid      (Key.left,         'gridX4' , 'gridY5'),           
    singlePressGrid      (Key.right,        'gridX5' , 'gridY5'),             

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

        scroll1 = dic['scroll1']

        if scroll1 == 1:
            scroll1Modular = scroll1Modular + 1
            if scroll1Modular % 6 == 0:
                mouse.scroll(1,0)
        
        scroll2 = dic['scroll2']

        if scroll2 == 1:
            scroll2Modular = scroll2Modular + 1
            if scroll2Modular % 6 == 0:
                mouse.scroll(-1,0)
        
        for buttonHandler in buttonList:
            buttonHandler.handle(dic, keyboard)
    except KeyboardInterrupt:
        exit()
    except Exception as e:
        print(str(e))
        time.sleep(1)
        toInit = True