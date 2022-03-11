int k = 7;
int cociente,residuo;
int leds[8] = {3,4,5,6,7,8,9,10};
int i;
int num;
void setup() {
  // put your setup code here, to run once:
  for(i = 0; i < 8; i++){
    pinMode(leds[i], OUTPUT);
  }

  Serial.begin(9600);
}

byte accion;
String temp;

void loop() {

  if (Serial.available()>0) {
    temp = Serial.readString();
    accion = temp.toInt();
  }

  switch(accion){
    case 0:
      break;
    case 1:
      //Primeros 2 bits 2 + 1 = 3
      num = 3;
      accion = 2;
      break;
    case 2:
      // Ultimo par de bits: 128 + 64 = 196
      if(num>196) num=3; //Reiniciar serie

      //Convertir v en binario para encender los leds
      k=7; //8 leds
      cociente = num;
      while(cociente>0){
        residuo = cociente%2;
        digitalWrite(leds[k--],residuo);
        cociente = cociente/2;
      }
      for(;k>=0;k--){
        digitalWrite(leds[k],0);
      }
      //num = num*2;
      num <<=1;
      delay(500);
      
      break;
  }
  
}
