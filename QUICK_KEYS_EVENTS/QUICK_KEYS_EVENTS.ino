#include <Keypad.h>

const byte ROWS = 2;
const byte COLS = 3;

char keys[ROWS][COLS] = {
  {'1', '2', '3'},
  {'4', '5', '6'}
};


byte rowPins[ROWS] = {3, 4};
byte colPins[COLS] = {8, 9, 10};
Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

bool change = false;
bool pressed = false;

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
}

void keypadEvent(KeypadEvent key) {
  switch (KeyState(keypad.getState())) {  
    case PRESSED:
      Serial.println(key);

    //case RELEASED:
      //pass
      //pressed = false;

    //case HOLD:
      //while(KeyState(keypad.getState()) == 2) {
      //  Serial.println(key);
      //}
  }
}
