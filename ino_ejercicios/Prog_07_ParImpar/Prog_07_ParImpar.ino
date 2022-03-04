enum ESTATES{
  PEDIR_NUM,
  ESPERAR_NUM,
  VERIFICAR,
  PAR_IMPAR,
  REINICIAR,
  SEGUIR,
  TERMINADO
  };
int estado, numero,parimpar;
String temporal;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  //Serial.setTimeout(250);
  estado = 0;
}

void loop() {
  switch(estado){
    case PEDIR_NUM:
      Serial.print(" \n  Numero: ");
      estado++;
      break;
    case ESPERAR_NUM:
      if(Serial.available()>0){
        temporal= Serial.readString();
        numero = temporal.toInt();
        estado++;
      }
      break;
    case VERIFICAR:
      parimpar = (numero%2);
      estado++;
      break;
    case PAR_IMPAR:
      Serial.println("");
      if(parimpar==0){
        Serial.println("El numero "+String(numero)+" es par");
        Serial.println("");
        estado++;
      }else{
        Serial.println("El numero "+String(numero)+" no es par");
        Serial.println("");
        estado++;
      }
      break;
      case REINICIAR:
        Serial.println("Quieres comprobar otro numero? \n 1.Si 2.No");
        estado++;
        break;
      case SEGUIR:
        if(Serial.available()>0){
          temporal= Serial.readString();
          numero = temporal.toInt();
          if(numero == 1) estado = PEDIR_NUM;
          else{
            Serial.println("Adios papi!!!");
            estado = TERMINADO; 
            } 
        }   
        break;
      case TERMINADO: 
        
        break;
  }
  delay(100);
}
