const byte ROWS = 2;
const byte COLS = 3;

byte rowPins[ROWS] = {3, 4};
byte colPins[COLS] = {8, 9, 10};

char keys[ROWS][COLS] = {
  {'1', '2', '3'},
  {'4', '5', '6'}
};

void setup() {
  Serial.begin(9600);
  for(int i = 0; i < sizeof(rowPins); i++) {
    pinMode(rowPins[i], OUTPUT);
    //digitalWrite(rowPins[i], LOW);
  }
  for(int j = 0; j < sizeof(colPins); j++) {
    pinMode(colPins[j], INPUT_PULLUP);
  }
}

void loop() {
  for(int i = 0; i < sizeof(rowPins); i++) {
    digitalWrite(rowPins[i], LOW);
    for(int j = 0; j < sizeof(colPins); j++) {
      if(digitalRead(colPins[j]) == 0) {
        Serial.println(keys[i][j]);
        delay(100);
        
      }
    }
    digitalWrite(rowPins[i], HIGH);
  }
}
