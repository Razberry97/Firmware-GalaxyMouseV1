#include <Mouse.h>
#include <Keyboard.h>

#define HORZ_PIN           20         // VRX Joystick
#define VERT_PIN           21         // VRY Joystick
#define joyButt            21         // VRY Joystick
#define scroll1            6          // Scroll out
#define scroll2            5          // Scroll in

#define Grid_X1           18          // 
#define Grid_X2           15          // 
#define Grid_X3           14          // 
#define Grid_X4           16          // 
#define Grid_X5           10          // 
#define Grid_X6           4           // grid on mouse buttons
#define Grid_Y1           5           //    
#define Grid_Y2           6           //   
#define Grid_Y3           7           //   
#define Grid_Y4           8           // 
#define Grid_Y5           9           //  

#define DEADZONE           30
#define DESIRED_MILLIS     400
#define SENSITIVITY        0.005     


int YZero = 0, XZero = 0;     

int YMax = 0, YMin = 0; 
int XMax = 0, XMin = 0; 

void setup(){
    pinMode (HORZ_PIN, INPUT_PULLUP);        
    pinMode (VERT_PIN, INPUT_PULLUP);     
    pinMode (joyButt, INPUT_PULLUP);  
    pinMode (scroll1, INPUT_PULLUP);
    pinMode (scroll2, INPUT_PULLUP);    
    
    pinMode (Grid_X1, INPUT_PULLUP);
    pinMode (Grid_X2, INPUT_PULLUP);
    pinMode (Grid_X3, INPUT_PULLUP);
    pinMode (Grid_X4, INPUT_PULLUP);
    pinMode (Grid_X5, INPUT_PULLUP);
    pinMode (Grid_X6, INPUT_PULLUP);
    pinMode (Grid_Y1, INPUT_PULLUP);
    pinMode (Grid_Y2, INPUT_PULLUP);
    pinMode (Grid_Y3, INPUT_PULLUP);
    pinMode (Grid_Y4, INPUT_PULLUP);
    pinMode (Grid_Y5, INPUT_PULLUP);
    
    
    
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
  bool scroll1Val = digitalRead(scroll1); 
  bool scroll2Val = digitalRead(scroll2); 

  bool X1Val = !digitalRead(Grid_X1);
  bool X2Val = !digitalRead(Grid_X2);
  bool X3Val = !digitalRead(Grid_X3);
  bool X4Val = !digitalRead(Grid_X4);
  bool X5Val = !digitalRead(Grid_X5);
  bool X6Val = !digitalRead(Grid_X6);
  bool Y1Val = !digitalRead(Grid_Y1);
  bool Y2Val = !digitalRead(Grid_Y2);
  bool Y3Val = !digitalRead(Grid_Y3);
  bool Y4Val = !digitalRead(Grid_Y4);
  bool Y5Val = !digitalRead(Grid_Y5);


  Serial.print("{");

  debugValueWithoutComma("YValue", YValue);
  debugValue("XValue", XValue);
  debugValue("joyButt", joyButtVal);
  debugValue("scroll1Val", scroll1Val);
  debugValue("scroll2Val", scroll2Val);

  debugValue("Grid_X1", X1Val);
  debugValue("Grid_X2", X2Val);
  debugValue("Grid_X3", X3Val);
  debugValue("Grid_X4", X4Val);
  debugValue("Grid_X5", X5Val);
  debugValue("Grid_X6", X6Val);
  debugValue("Grid_Y1", Y1Val);
  debugValue("Grid_Y2", Y2Val);
  debugValue("Grid_Y3", Y3Val);
  debugValue("Grid_Y4", Y4Val);
  debugValue("Grid_Y5", Y5Val);
  
  Serial.println("}");

  delay(10);
}

bool rot = HIGH;
bool timeoff = LOW;

