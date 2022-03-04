int leds [8] = {2, 3, 4, 5, 6, 7, 8, 9};

void setup() {
    for(int i = 0; i < 8; i++){
        pinMode(leds[i], OUTPUT);
    }
    Serial.begin(9600);
}

int i = 0;
void loop() {
    limpiar();
    digitalWrite(leds[i], 1);
    i += 1;
    if(i == 8)
        i = 0;
    delay(500);
}

void limpiar(){
  for(int i = 0; i < 8; i++){
    digitalWrite(leds[i], 0);
  }
}
