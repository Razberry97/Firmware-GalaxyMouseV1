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

void setup(){
    pinMode (HORZ_PIN, INPUT_PULLUP);        
    pinMode (VERT_PIN, INPUT_PULLUP);     

    pinMode (joyButt, INPUT_PULLUP);  
    pinMode (button6, INPUT_PULLUP);
    pinMode (button7, INPUT_PULLUP);   

    
    YZero = analogRead(VERT_PIN);  
    XZero = analogRead(HORZ_PIN);  
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

  delay(10);
}

bool rot = HIGH;
bool timeoff = LOW;

