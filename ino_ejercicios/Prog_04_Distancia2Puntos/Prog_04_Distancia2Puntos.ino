/*
  Distancia entre dos puntos, dadas las coordenadas
*/

enum Edos{setX1,setY1,setX2,setY2,repeat,finalizado};

Edos estado = setX1;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

float x1,x2,y1,y2,dist,v;
String value;

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    value = Serial.readString();
    checkInput();
  }
}

void checkInput(){
    if(!value.equals(" ")){
        v = value.toInt();
        Serial.println(v);
    }
}