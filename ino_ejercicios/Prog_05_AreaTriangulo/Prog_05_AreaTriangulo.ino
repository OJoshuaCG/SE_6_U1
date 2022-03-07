enum Estados {
  PEDIR_BASE,
  ESPERAR_BASE,
  PEDIR_ALTURA,
  ESPERAR_ALTURA,
  CALCULAR_AREA,
  IMPRIMIR_AREA,
  REINICIAR
};

int estado;
float area;
float base;
String tempBase;
float altura;
String tempA;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(250);
  estado = 0;

}

void loop() {
  switch (estado) {
    case PEDIR_BASE:
      Serial.print("Base: ");
      estado++;
      break;
    case ESPERAR_BASE:
      if (Serial.available() > 0) {
        tempBase = Serial.readString();
        base = tempBase.toFloat();
        Serial.print(tempBase);
        estado++;
      }
      break;
    case PEDIR_ALTURA:
      Serial.println("");
      Serial.print("Altura: ");
      
      estado++;
      break;
    case ESPERAR_ALTURA:
      if (Serial.available() > 0) {
        tempA = Serial.readString();
        altura = tempA.toFloat();
        Serial.print(tempA);
        estado++;
      }
      break;
    case CALCULAR_AREA:
      area = (base * altura)/2;
      estado++;
      break;
    case IMPRIMIR_AREA:
      Serial.println("");
      Serial.println("El area del Triangulo es : " + String(area));
      Serial.println("");
      estado++;
      break;
    case REINICIAR:
      estado = 0;
      break;
  }
  delay(100);
}
