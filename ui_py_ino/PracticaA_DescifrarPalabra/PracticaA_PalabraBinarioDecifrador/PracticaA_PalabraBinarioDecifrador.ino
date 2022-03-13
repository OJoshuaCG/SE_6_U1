byte leds[8] = {9, 8, 7, 6, 5, 4, 3, 2};
byte letra;

void setup(){
  for (byte i = 0; i < sizeof(leds); i++){
    pinMode(leds[i], OUTPUT);
  }

  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop(){
  if (Serial.available() > 0){
    letra = (byte) Serial.readString().toInt();

    if(letra == 0)    
      limpiar();
    
    else
      encenderLeds(letra);    
  }
}

void limpiar(){
  for (byte i = 0; i < 8; i++)
    digitalWrite(leds[i], 0);
}

void encenderLeds(byte ascii){
  for (byte j = 0; j < 8; j++){
    if ( ( (ascii >> j) & 1 )  == 1 )
      digitalWrite(leds[j], 1);    
    else
      digitalWrite(leds[j], 0);    
  }
}
