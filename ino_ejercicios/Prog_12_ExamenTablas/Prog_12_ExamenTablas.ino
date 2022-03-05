enum edos {
  pedirTabla,setTabla,pregunta,respuesta,resultados,repetir,finalizado
};
edos estado = pedirTabla;

int tabla,value,puntaje,i,r;
String temp;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(100);
}

void loop() {
  // put your main code here, to run repeatedly:
  switch(estado){
    case pedirTabla:
      Serial.println("\n---Examen Tablas de Multiplicar---");
      Serial.print("Tabla: ");
      estado = setTabla;
      i = 1;
      puntaje = 0;
      break;
    case setTabla:
      if(Serial.available()>0){
        temp = Serial.readString();
        Serial.print(temp+"\n");
        tabla = temp.toInt();
        estado = pregunta;
      }
      break;
    case pregunta:
      Serial.print(String(tabla)+"x"+String(i)+"= ");
      estado = respuesta;
      break;
    case respuesta:
      if(Serial.available()>0){
        temp = Serial.readString();
        Serial.print(temp);
        value = temp.toInt();
        r = tabla*i;
        Serial.print("      *** " + String(r));
        if(r == value){
          Serial.print(" CORRECTO! \n");
          puntaje++;
        }else  Serial.print(" INCORRECTO!  \n");

        i++;
        if(i<=10) estado = pregunta;
        else{ 
          estado = resultados;
        }
      }
      break;
    case resultados:
      Serial.println("\nPuntaje: " + String(puntaje));
      Serial.print("Desea practicar otra tabla? \n 1.Si \n 2.Finalizar \nR: ");
      estado = repetir;
      break;
    case repetir:
      if(Serial.available()>0){
        temp = Serial.readString();
        Serial.print(temp);
        value = temp.toInt();
        if(value == 1) estado = pedirTabla;
        else {
          estado = finalizado;
          Serial.println("Adios!!!");
        }
      }
      break;
  }
}
