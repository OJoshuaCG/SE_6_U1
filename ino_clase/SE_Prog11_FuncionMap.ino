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

int v, vNueva;
void loop() {
    // 10 bits de resolucion, 5v de referencia, ADC -> 0 - 1023
    v = analogRead(A0);
    vNueva = map(v, 0, 1023, 0, 7);
    // v = valor a mapear
    // 0 = lim inf intervalo origen
    // 1023 = lim sup intervalo destino
    // 0 = lim inf intervalo destino
    // 7 = lim sup intervalo destino

    //Serial.println("Valor leido: " + String(v));
    Serial.println("v: " + String(v) + "  vNueva: " + String(vNueva));

    delay(100);


    /*
    - Prender el led que marque el map
    - 

    */


}