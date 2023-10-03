#include <Mouse.h>
#include <Keyboard.h>

#define HORZ_PIN           20         // VRX Joystick
#define VERT_PIN           21         // VRY Joystick
#define DEADZONE           30
#define DESIRED_MILLIS     400
#define SENSITIVITY        0.005     
#define joyButt           2          // SW Joystick
#define button1           4          // pinky Button
#define button2           3          // anulare Button    
#define button3           19         // middle Button    
#define button4           15         // index Button    
#define button5           18         // thumb Button    
#define button6           6          // Scroll out
#define button7           5          // Scroll in

int YZero = 0, XZero = 0;     

int YMax = 0, YMin = 0; 
int XMax = 0, XMin = 0; 

void setup(){
    pinMode (HORZ_PIN, INPUT_PULLUP);        
    pinMode (VERT_PIN, INPUT_PULLUP);     

    pinMode (joyButt, INPUT_PULLUP);  
    pinMode (button1, INPUT_PULLUP);
    pinMode (button2, INPUT_PULLUP);
    pinMode (button3, INPUT_PULLUP);   
    pinMode (button4, INPUT_PULLUP);
    pinMode (button5, INPUT_PULLUP);      
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
  bool button1Val = !digitalRead(button1);
  bool button2Val = !digitalRead(button2); 
  bool button3Val = !digitalRead(button3); 
  bool button4Val = !digitalRead(button4); 
  bool button5Val = !digitalRead(button5); 
  bool button6Val = digitalRead(button6); 
  bool button7Val = digitalRead(button7); 

  Serial.print("{");

  debugValueWithoutComma("YValue", YValue);
  debugValue("XValue", XValue);
  debugValue("joyButt", joyButtVal);
  debugValue("button1", button1Val);
  debugValue("button2", button2Val);
  debugValue("button3", button3Val);
  debugValue("button4", button4Val);
  debugValue("button5", button5Val);
  debugValue("button6", button6Val);
  debugValue("button7", button7Val);

  Serial.println("}");

  delay(10);
}

bool rot = HIGH;
bool timeoff = LOW;

