#include <Mouse.h>
#include <Keyboard.h>

#define HORZ_PIN           21         // VRY Joystick
#define VERT_PIN           20         // VRX Joystick
#define DEADZONE           50
#define DESIRED_MILLIS     400
#define SENSITIVITY        0.005
#define DT                15          // DT Encoder                      
#define CLK               18          // CLK Encoder        
#define joyButt           19         // SW Joystick
#define button1           2          // Rear Button
#define button2           3          // Rear Button    
#define button3           4          // Rear Button    
#define button4           7          // Rear Button    
#define button5           8          // Rear Button    
#define button6           14          // Scroll out
#define button7           16          // Scroll in

int YZero = 0, XZero = 0;     

int YMax = 0, YMin = 0; 
int XMax = 0, XMin = 0; 

void setup(){
    pinMode (HORZ_PIN, INPUT_PULLUP);        
    pinMode (VERT_PIN, INPUT_PULLUP);     

    pinMode (button1, INPUT_PULLUP);
    pinMode (button2, INPUT_PULLUP);
    pinMode (button3, INPUT_PULLUP);   
    pinMode (button4, INPUT_PULLUP);
    pinMode (button5, INPUT_PULLUP);      
    pinMode (button6, INPUT_PULLUP);
    pinMode (button7, INPUT_PULLUP);      
    pinMode (joyButt, INPUT_PULLUP);  
    pinMode (DT, INPUT_PULLUP);
    pinMode (CLK, INPUT_PULLUP);
    
    
    YZero = analogRead(VERT_PIN);  
    XZero = analogRead(HORZ_PIN);  
}

bool isPressing = false;
unsigned long lastMillis = 0;

#define debugValue(display, value) Serial.print(",\""); Serial.print(display); Serial.print("\":"); Serial.print(value);
#define debugValueWithoutComma(display, value) Serial.print("\""); Serial.print(display); Serial.print("\":"); Serial.print(value);

void loop(){
  int YValue = analogRead(VERT_PIN) - YZero;  
  int XValue = analogRead(HORZ_PIN) - XZero;

  bool button1Val = !digitalRead(button1);
  bool button2Val = !digitalRead(button2); 
  bool button3Val = !digitalRead(button3); 
  bool joyButtVal = !digitalRead(joyButt);
  bool button4Val = !digitalRead(button4); 
  bool button5Val = !digitalRead(button5); 
  bool button6Val = digitalRead(button6); 
  bool button7Val = digitalRead(button7); 

  Serial.print("{");

  debugValueWithoutComma("YValue", YValue);
  debugValue("XValue", XValue);
  debugValue("button1", button1Val);
  debugValue("button2", button2Val);
  debugValue("button3", button3Val);
  debugValue("joyButt", joyButtVal);
  debugValue("scroll", scroll());
  debugValue("button4", button4Val);
  debugValue("button5", button5Val);
  debugValue("button6", button6Val);
  debugValue("button7", button7Val);

  Serial.println("}");

  delay(10);
}

bool rot = HIGH;
bool timeoff = LOW;

uint8_t scroll (void)
{
  uint8_t ret = 0;
  bool scr = digitalRead(DT);
  bool scr2 = digitalRead(CLK);
  uint16_t timS;
  uint16_t hS = 0;
  timS = millis() - hS;
  if(scr != scr2)
    {
      timeoff = LOW;
    }
  if (timS > 10)
    {
    hS = millis();
    if(rot == HIGH)
      {
        ret = scr-scr2;
        rot=!rot; 
      }
    if(scr==HIGH && scr2==HIGH)
      {
        rot=!rot; 
      }
  }
  return ret;
}