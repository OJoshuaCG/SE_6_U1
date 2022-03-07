String numero;
int contador = 0;
byte estado = 0;

void setup()
{
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop()
{
  switch (estado)
  {
    case 0:
      Serial.println("Ingresa un número:");
      estado = 1;
      break;
    case 1:
      if (Serial.available() > 0)
      {
        numero = Serial.readString();
        estado = 2;
      }
      break;
    case 2:
      if (numero != "\n")
      {
        if (numero.toInt() >= 0)
        {
          estado = 3;
        }
        else
        {
          Serial.print(numero);
          estado = 4;
        }
      }
      else
      {
        estado = 1;
      }
      break;
    case 3:
      contador++;
      Serial.print(numero);
      estado = 0;
      break;
    case 4:
      Serial.println("Fueron ingresados " + String(contador) + " números.");
      estado = 5;
      break;
    case 5:
      Serial.println("¿Deseas repetir el algoritmo? (1 = SÍ / 0 = NO)");
      estado = 6;
      break;
    case 6:
      if (Serial.available() > 0) {
        numero = Serial.readString();
        estado = 7;
      }
      break;
    case 7:
      if (numero != "\n")
      {
        estado = 8;
      }
      else {
        estado = 6;
      }
      break;
    case 8:
      if (numero.toInt() == 1)
      {
        contador = 0;
        estado = 0;
      }
      else
      {
        if (numero.toInt() != 0)
        {
          Serial.println("Ingrese un valor válido");
          estado = 6;
        }
        else
        {
          Serial.println("Gracias");
          estado = 99;
        }
      }
      break;
  }
}
