from handlers.baseHandler import baseHandler
from pynput.keyboard import Key
import win32api
import time
import pydirectinput

GRID_MAP = {
    'j' : '1',
    's' : '2',
    'u' : '3',
    'k' : '4',
    'd' : '5',
    'i' : '6',
    'l' : '7',
    'f' : '8',
    'o' : '9',
    '0' : '0',
    't' : Key.right,
    'p' : Key.left,
    'b' : '.',
    'r' : Key.enter,
    'v' : '*',
    # 'e' : Key.ctrl-Key.right, #go to end line
    'c' : '/',
    # 'w' : Key.ctrl-Key.left, #go to start line
    # 'x' : Key.ctrl-Key.left-Key.shift-Key.right, #select entire line
    'q' : Key.backspace,
    'y' : '+',
    'a' : '-',
    # 'h' : Key.ctrl-'v',
    # 'z' : Key.ctrl-'c',
    '5' : 's',
    '4' : 'x',
    '3' : Key.ctrl,
    '2' : Key.shift, #needs to be continuously pressed
    '1' : Key.esc,
}

class gridHandler(baseHandler):    
    def __init__(self):
        pass
    
    def handle(self, dic):
        gridvals = dic["gridVals"]
        for key in gridvals:
            keychar = key["keykchar"]
            keykstate = key["keykstate"]
            if(keychar in GRID_MAP):
                if keykstate == '1':
                    pydirectinput.keyDown('f')
                elif keykstate == '3':
                    pydirectinput.keyUp('f')
        # if len(gridvals) > 0:
        #     print(gridvals)

    