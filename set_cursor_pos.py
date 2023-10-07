import serial
import json
import time
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller as MouseController
from handlers.continuousPressButton import continuousPressButton
from handlers.singlePressButton import singlePressButton
from handlers.joystickHandler import JoyStickHandler
from handlers.zoomHandler import ZoomHandler

settings = json.load(open("C:\\Users\\scorp\\Desktop\\things\\3d mouse firmware\\settings.json"))

keyboard = Controller()
mouse = MouseController()


buttonList = [
    ZoomHandler(mouse,keyboard),
    JoyStickHandler(mouse,keyboard),
    singlePressButton([Key.ctrl, 'z'],  'joyButt'),   
    singlePressButton(Key.esc,          'button1'),
    continuousPressButton(Key.shift,    'button2'),
    singlePressButton(Key.ctrl,         'button3'),
    singlePressButton(['x'],            'button4'),
    singlePressButton(['s'],            'button5'),
]

toInit = True

while True:
    try:
        if toInit:
            ser = serial.Serial(settings["ARDUINO_PORT"], 9600)
            toInit = False

        line = ser.readline().decode('utf-8')
        dic = json.loads(line)
        
        for buttonHandler in buttonList:
            buttonHandler.handle(dic, keyboard)
    except KeyboardInterrupt:
        exit()
    except Exception as e:
        print(str(e))
        time.sleep(1)
        toInit = True

