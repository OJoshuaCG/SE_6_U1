String numero;
String potencia;
double resultado;
byte estado;

void setup()
{
  Serial.begin(9600);
  Serial.setTimeout(100);
}

void loop() {
  switch (estado) {
    case 0:
      Serial.println("Ingresa el número a elevar: ");
      estado = 1;
      break;
    case 1:
      if (Serial.available() > 0) {
        numero = Serial.readString();
        estado = 2;
      }
      break;
    case 2:
      if (numero != "\n")
      {
        estado = 3;
        Serial.print(numero);
      }
      else {
        estado = 1;
      }
      break;
    case 3:
      Serial.println("Ingresa la potencia: ");
      estado = 4;
      break;
    case 4:
      if (Serial.available() > 0) {
        potencia = Serial.readString();
        estado = 5;
      }
      break;
    case 5:
      if (potencia != "\n")
      {
        estado = 6;
        Serial.print(potencia);
      }
      else {
        estado = 4;
      }
      break;
    case 6:
      resultado = pow(numero.toInt(), potencia.toInt());
      estado = 7;
      break;
    case 7:
      Serial.println("El resultado es: " + String(resultado));
      estado = 8;
      break;
    case 8:
      Serial.println("¿Deseas repetir el algoritmo? (1 = SÍ / 0 = NO)");
      estado = 9;
      break;
    case 9:
      if (Serial.available() > 0) {
        numero = Serial.readString();
        estado = 10;
      }
      break;
    case 10:
      if (numero != "\n")
      {
        estado = 11;
      }
      else {
        estado = 9;
      }
      break;
    case 11:
      if(numero.toInt() == 1)
      {
        estado = 0;
      }else
      {
        if(numero.toInt() != 0)
        {
          Serial.println("Ingrese un valor válido");
          estado = 9;
        }
        else
        {
          Serial.println("Gracias");
          estado = 99;
        }
      }
      break;
  }

  delay(100);
}
