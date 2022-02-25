int leds[8] = {6, 7, 8, 9, 10, 11, 12, 13};
// bit menos significativo 13
// bit mas significativo 6

int estado = 0;
void setup() {
    for(int i = 0; i < 8; i++){
        pinMode(leds[i], OUTPUT);
    }

    Serial.begin(9600);
    Serial.setTimeout(10);
}


String valor;
int v;
void loop(){
    switch(estado){
        case 0:
            Serial.println("Ingresa un numero");
            estado = 1;
        break;
        case 1: case 6:
            if(Serial.available()>0){
                valor = Serial.readString();
                if(estado == 1)
                    estado = 2;
                else
                    estado = 7;
            }
        break;
        case 2: case 7: // Estado de validacion
            if(!valor.equals("")){  
                v = valor.toInt();
                Serial.println(v);
                if(estado == 2) // Si se cuenta con el numero para elevar al cuadrado
                    estado = 3;
                else{
                    // con el valor leido, necesito comprobar la respuesta del usuario
                    if(v == 1)
                        estado = 0;
                    else
                        estado = 5;
                }    
            }
            else{ 
                // Si v esta vacio, entonces necesita volver a la fase
                // en la que lee esto, para obtener un valor nuevo
                estado -= 1;
            }
        break;
        case 3:
            v = v * v;
            estado = 4;
        break;
        case 4:
            Serial.println("Resultado: " + String(v));
            estado = 5;
        break;
        case 5:
            Serial.println("Deseas repetir el algoritmo? (1=Si, 0=No)");
            estado = 6;
        break;
    }
    
}
