int pulsador = 2;
void setup() {
    pinMode(pulsador, INPUT_PULLUP);
    Serial.begin(9600);
}

int valor;
void loop() {
    valor = !digitalRead(pulsador);
    Serial.println(String(valor));

    delay(100);
}
