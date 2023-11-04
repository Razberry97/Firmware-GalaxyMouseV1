import serial
import json
import time
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller as MouseController
from handlers.joystickHandler import JoyStickHandler
from handlers.zoomHandler import ZoomHandler

settings ={
        "ARDUINO_PORT": "COM5"
        } 

keyboard = Controller()
mouse = MouseController()


handlersList = [
    ZoomHandler(),
    JoyStickHandler()
]

for genericHandler in handlersList:
    genericHandler.setMouse(mouse)
    genericHandler.setKeyboard(keyboard)

toInit = True

while True:
    try:
        if toInit:
            ser = serial.Serial(settings["ARDUINO_PORT"], 9600)
            ser.readline()
            toInit = False

        line = ser.readline().decode('utf-8')
        dic = json.loads(line)
        
        for genericHandler in handlersList:
            genericHandler.handle(dic)
    except KeyboardInterrupt:
        ser.close()
        exit()
    except Exception as e:
        try:
            ser.close()
        except:
            pass
        print(str(e))
        time.sleep(2)
        toInit = True

