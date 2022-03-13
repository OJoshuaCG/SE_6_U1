byte leds[8] = {2, 3, 4, 5, 6, 7, 8, 9};
byte v;
byte led = 0;

void setup(){
  for (byte i = 0; i < 8; i++)  {
    pinMode(leds[i], OUTPUT);
  }

  Serial.begin(9600);
  Serial.setTimeout(1);
}

void loop(){
  if (Serial.available() > 0)  {
    v = (byte)Serial.readString().toInt();
    if (v > 1)    {
      limpiar();
    } else{
      digitalWrite(leds[led], v);
      led++;
    }
  }
}

void limpiar(){
  led = 0;
  for (byte i = 0; i < 8; i++)  {
    digitalWrite(leds[i], 0);
  }
}
