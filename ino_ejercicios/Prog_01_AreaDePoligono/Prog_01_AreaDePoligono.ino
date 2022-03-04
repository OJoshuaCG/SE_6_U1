enum estates {
  pedir_perimetro,
  leer_perimetro,
  pedir_apotema,
  leer_apotema,
  calcular_area,
  imprimir_area,
  reiniciar,
  seguir, 
  terminado
};

int estado, tempN;
float area;
float perimetro;
float apotema;
String temp; 

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  //Serial.setTimeout(250);
  estado = 0;
}

void loop() {
  switch (estado) {
    case pedir_perimetro:
      Serial.print("  \n  Perimetro: ");
      Serial.println(" ");
      estado++;
      break;
    case leer_perimetro:
      if (Serial.available() > 0) {
        temp = Serial.readString();
        perimetro = temp.toInt();
        estado++;
      }
      break;
    case pedir_apotema:
      Serial.print("Apotema: ");
      Serial.println(" ");
      estado++;
      break;
      
    case leer_apotema:
      if (Serial.available() > 0) {
        temp = Serial.readString();
        apotema = temp.toInt();
        estado++;
      }
      break;
    case calcular_area:
      area = (perimetro*apotema)/2;
      estado++;
      break;
    case imprimir_area:
      Serial.print("El area del poligono es: "+String(area));
      Serial.println(" ");
      estado++;
      break;
      
      case reiniciar:
      Serial.println("Quieres comprobar otro numero? \n 1.Si 2.No");
          estado++;
        //estado = 0;
        break;

      case seguir: 
        if(Serial.available()>0){
            temp= Serial.readString();
            tempN = temp.toInt();
            if(tempN == 1) estado = pedir_perimetro;
            else{
              Serial.println("Adios !!!");
              estado = terminado;
            }
        } 
        break; 
  }
  delay(100);
}
