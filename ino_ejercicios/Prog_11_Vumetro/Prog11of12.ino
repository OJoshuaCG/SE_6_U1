const byte leds[8] = {2, 3, 4, 5, 6, 7, 8, 9};
byte numero;
byte estado;

void setup() {
  for(byte i = 0; i < 8; i++)
  {
    pinMode(leds[i], OUTPUT);
  }
  Serial.begin(9600);
  Serial.setTimeout(100);
}

void loop() {
  switch(estado)
  {
    case 0:
      numero = random(9);
      Serial.println(String(numero));
      estado = 1;
      break;
    case 1:
      for(byte i = 0; i < numero; i++)
      {
        digitalWrite(leds[i], 1);
        delay(100);
      }
      estado = 2;
      break;
    case 2:
      for(int i = numero - 1; i >= 0; i--)
      {
        digitalWrite(leds[i], 0);
        delay(100);
      }
      estado = 0;
      break;
  }

}
