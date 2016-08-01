#include <Keypad.h>

const byte ROWS = 2;
const byte COLS = 3;

char keys[ROWS][COLS] = {
  {'1', '2', '3'},
  {'4', '5', '6'}
};

byte rowPins[ROWS] = {3, 4};
byte colPins[COLS] = {8, 9, 10};
Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS);

void setup() {
  Serial.begin(9600);
}

void loop() {
  char key = keypad.getKey();
  Serial.println(KeyState(keypad.getState()));
  
  if(key != NO_KEY) {
    Serial.println(key);
  }
}
