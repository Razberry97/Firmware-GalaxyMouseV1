#include <Mouse.h>
#include <Keyboard.h>
#include <Key.h>
#include <Keypad.h>

#define HORZ_PIN           20         // VRX Joystick
#define VERT_PIN           21         // VRY Joystick
#define DEADZONE           10
#define DESIRED_MILLIS     400
#define SENSITIVITY        0.005     
#define joyButt           19          // SW Joystick
#define button6           2          // Scroll out
#define button7           3          // Scroll in

int YZero = 0, XZero = 0;     

int YMax = 0, YMin = 0; 
int XMax = 0, XMin = 0; 


const char CTRL_C = 'z';
const char CTRL_V = 'h';
const char LINE_SEL = 'k';

const byte ROWS = 6; 
const byte COLS = 5; 

char hexaKeys[ROWS][COLS] = {
  { KEY_DELETE, KEY_HOME, KEY_END, KEY_KP_ENTER, KEY_RIGHT_ARROW },
  { KEY_KP_PLUS, '3', '6', '9', KEY_LEFT_ARROW }, 
  { KEY_KP_MINUS, '2', '5', '8', '0' },
  { CTRL_V, '1', '4', '7', '0' },
  { CTRL_C, LINE_SEL, KEY_KP_SLASH, KEY_KP_ASTERISK, '.' },
  { 's', 'x', KEY_LEFT_CTRL, KEY_LEFT_SHIFT, KEY_ESC },
};


byte rowPins[ROWS] = {18, 15, 14, 16, 10, 4}; 
byte colPins[COLS] = {9, 8, 7, 6, 5};

Keypad kpd = Keypad(makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS); 

void setup(){
    pinMode (HORZ_PIN, INPUT_PULLUP);        
    pinMode (VERT_PIN, INPUT_PULLUP);     

    pinMode (joyButt, INPUT_PULLUP);  
    pinMode (button6, INPUT_PULLUP);
    pinMode (button7, INPUT_PULLUP);   

    
    YZero = analogRead(VERT_PIN);  
    XZero = analogRead(HORZ_PIN);  
    
    Serial.begin(9600);
    Keyboard.begin();
}

bool isPressing = false;
unsigned long lastMillis = 0;

#define debugValue(display, value) Serial.print(",\""); Serial.print(display); Serial.print("\":"); Serial.print(value);
#define debugValueWithoutComma(display, value) Serial.print("\""); Serial.print(display); Serial.print("\":"); Serial.print(value);

void loop(){
  int YValue = (analogRead(VERT_PIN) - YZero) * -1;  
  int XValue = (analogRead(HORZ_PIN) - XZero) * -1;

  bool joyButtVal = !digitalRead(joyButt);
  bool button6Val = digitalRead(button6); 
  bool button7Val = digitalRead(button7); 

  Serial.print("{");

  debugValueWithoutComma("YValue", YValue);
  debugValue("XValue", XValue);
  debugValue("joyButt", joyButtVal);
  debugValue("button6", button6Val);
  debugValue("button7", button7Val);

  Serial.println("}");


  // Fills kpd.key[ ] array with up-to 10 active keys.
  // Returns true if there are ANY active keys.
  if (kpd.getKeys())
  {
      for (int i=0; i<LIST_MAX; i++)   // Scan the whole key list.
      {
          if ( kpd.key[i].stateChanged )   // Only find keys that have changed state.
          {
              switch (kpd.key[i].kstate) {  // Report active key state : IDLE, PRESSED, HOLD, or RELEASED
                  case PRESSED:
                  switch(kpd.key[i].kchar){
                    case CTRL_C:
                      Keyboard.press(KEY_LEFT_CTRL);
                      Keyboard.press('c');
                      Keyboard.release('c');
                      Keyboard.release(KEY_LEFT_CTRL);
                      break;
                    case CTRL_V:
                      Keyboard.press(KEY_LEFT_CTRL);
                      Keyboard.press('v');
                      Keyboard.release('v');
                      Keyboard.release(KEY_LEFT_CTRL);
                      break;
                    case LINE_SEL:
                      Keyboard.write(KEY_HOME);
                      Keyboard.press(KEY_LEFT_SHIFT);
                      Keyboard.write(KEY_END);
                      Keyboard.release(KEY_LEFT_SHIFT);
                      break;
                    default:
                      Keyboard.press(kpd.key[i].kchar);
                      break;
                  }
              break;
                  case HOLD:
              break;
                  case RELEASED:                  
                  switch(kpd.key[i].kchar){
                    case LINE_SEL:
                    case CTRL_C:
                    case CTRL_V:
                      break;
                    default:
                      Keyboard.release(kpd.key[i].kchar);
                      break;
                  }
              break;
                  case IDLE:
                  break;
            }
          }
        }
      }
  }


bool rot = HIGH;
bool timeoff = LOW;

