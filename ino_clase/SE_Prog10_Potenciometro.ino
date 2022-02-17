int leds[8] = {6, 7, 8, 9, 10, 11, 12, 13};
// bit menos significativo 13
// bit mas significativo 6

void setup() {
    for(int i = 0; i < 8; i++){
        pinMode(leds[i], OUTPUT);
    }

    Serial.begin(9600);
    Serial.setTimeout(10);
}

int v;
void loop() {
    // 10 bits de resolucion, 5v de referencia, ADC -> 0 - 1023
    v = analogRead(A0);
    Serial.println("Valor leido: " + String(v));

    delay(100);
}