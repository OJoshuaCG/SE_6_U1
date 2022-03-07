enum edos {pedirN,setN,defS1,defS2,repetir,finalizado};
int estado;
int i,n,s1,s2;
String temp;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(100);
}

void loop() {
  // put your main code here, to run repeatedly:
  switch(estado){
    case pedirN:
      Serial.print("\nIteraciones de las Series: ");
      estado = setN;
      i=1;
      break;
    case setN:
      if(Serial.available()>0){
        temp = Serial.readString();
        Serial.print(temp+"\n");
        n = temp.toInt();
        estado = defS1;
      }
      break;
    case defS1:
      //Establecer la Sucesion Objetivo 1
      s1 = 2*i+1;
      Serial.println("Serie1: "+String(s1));
      estado = defS2;
      break;
    case defS2:
      s2 = (i-1)*2;
      Serial.println("Serie2: "+String(s2)+"\n");
      i++;
      if(i>n) {
        estado = repetir;
        Serial.print("Desea calcular de nuevo? \n 1.Si 2.No \nR:");
      }
      else estado = defS1;
      break;
    case repetir:
      if(Serial.available()>0){
        temp = Serial.readString();
        Serial.print(temp+"\n");
        i = temp.toInt();
        if(i==1) estado = pedirN;
        else {
          Serial.println("Adios!!!");
          estado = finalizado;
        }
      }
      break;
  }
}
