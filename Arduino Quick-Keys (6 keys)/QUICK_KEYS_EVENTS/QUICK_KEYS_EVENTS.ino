#include <Keypad.h>

const byte ROWS = 3;
const byte COLS = 3;

char keys[ROWS][COLS] = {
  {'1', '2', '3'},
  {'4', '5', '6'},
  {'7', '8', '9'}
};


byte rowPins[ROWS] = {3, 4, 5};
byte colPins[COLS] = {8, 9, 10};
Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

bool change = false;
bool pressed = false;

char cha;

void setup() {
  Serial.begin(9600);
  keypad.addEventListener(keypadEvent);
}

void loop() {
  char key = keypad.getKey();
  /*if(key) {
    Serial.println(key);
    delay(50);
  }*/
  //KeyState state = keypad.getState();
  //Serial.println(KeyState(keypad.getState()));
  if(KeyState(keypad.getState() == 2)) {
    Serial.println(cha);
    delay(50);
  }
}

void keypadEvent(KeypadEvent key) {
  switch (KeyState(keypad.getState())) {  
    case PRESSED:
      Serial.println(key);
      cha = key;

    case RELEASED:
      //pass
      pressed = false;
      
    //case HOLD:
      //pressed = true;
      //while(KeyState(keypad.getState()) == 2) {
      //  Serial.println(key);
      //}
  }
}

