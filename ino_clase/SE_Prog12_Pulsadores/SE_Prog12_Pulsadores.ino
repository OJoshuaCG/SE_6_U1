int leds[8] = {6, 7, 8, 9, 10, 11, 12, 13};
// bit menos significativo 13
// bit mas significativo 6

int pulsador = 2, sw = 3;
void setup() {
    for(int i = 0; i < 8; i++){
        pinMode(leds[i], OUTPUT);
    }

    pinMode(pulsador, INPUT_PULLUP);
    pinMode(sw, INPUT_PULLUP);
    Serial.begin(9600);
    //Serial.setTimeout(10);
}

int vPulsador, vSW;
void loop() {
    vPulsador = digitalRead(pulsador);
    vSW = digitalRead(sw);
    
    Serial.println("Pulsador: " + String(vPulsador) + "Switch: " + String(SW));

    delay(100);
}