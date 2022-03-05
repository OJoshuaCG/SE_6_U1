/*
  Distancia entre dos puntos, dadas las coordenadas
*/

enum Edos{
  getX1,getY1,getX2,getY2,
  setX1,setY1,setX2,setY2,
  calcular,repetir,finalizado
  };

int estado = getX1;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(100);
}

float x1,x2,y1,y2,dist;
int value;
String temp;

void loop() {
  // put your main code here, to run repeatedly:
  switch(estado){
    case getX1:
      Serial.println("Distancia entre dos puntos");
      Serial.print("X1: ");
      estado = setX1;
      break;
    case setX1:
      if (Serial.available() > 0) {
        temp = Serial.readString();
        Serial.print(temp + "\n");
        x1 = temp.toFloat();
        estado = getY1;
      }
      break;
    case getY1:
      Serial.print("Y1: ");
      estado = setY1;
      break;
    case setY1:
      if (Serial.available() > 0) {
        temp = Serial.readString();
        Serial.print(temp + "\n");
        y1 = temp.toFloat();
        estado = getX2;
      }
      break;
      
    case getX2:
      Serial.print("X2: ");
      estado = setX2;
      break;
    case setX2:
      if (Serial.available() > 0) {
        temp = Serial.readString();
        Serial.print(temp + "\n");
        x2 = temp.toFloat();
        estado = getY2;
      }
      break;
    case getY2:
      Serial.print("Y2: ");
      estado = setY2;
      break;
    case setY2:
      if (Serial.available() > 0) {
        temp = Serial.readString();
        Serial.print(temp + "\n");
        y2 = temp.toFloat();
        estado = calcular;
      }
      break;
    case calcular:
      dist = sqrt(pow(x2-x1,2)+pow(y2-y1,2));
      Serial.println("\n La distancia es: " + String(dist));
      Serial.println("Quieres calcular otra distancia? \n 1.Si 2.No");
      estado = repetir;
      break;
    case repetir:
      if(Serial.available()>0){
        temp= Serial.readString();
        value = temp.toInt();
        if(value == 1) estado = getX1;
        else{
           Serial.println("Adios !!!");
           estado = finalizado;
        }
      } 
      break;
    case finalizado:
      break;  
  }
}
