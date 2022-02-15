int estado = 0;
void setup(){
    Serial.begin(9600);
    Serial.setTimeout(10);
}

String cadena;
int v;
// "AxxxxxxxxG" donde x = {0, 1}
void loop(){
    if(Serial.available()>0){
        cadena += Serial.readString();

        // Opciones
        // 1 = Cadena completa
        // 2 = Varias cadenas completas/incompletas
        // 3 = Cadena incompletas
        //  3.1 = Recibir la parte que acompleta a la cadena incompleta
        //  3.2 = Recibid una cadena incompleta de inicio junto con una cadena completa despues
        // 4 = Cadena completa y parte final incompleta
        

        int ultimaVezDeA = cadena.lastIndexOf("A"); // -1 cuando no lo encuentre
        int ultimaVezDeG = cadena.lastIndexOf("G"); // -1 cuando no lo encuentre

        String subCadena = cadena.substring(ultimaVezDeA+1, ultimaVezDeG);

        Serial.println(subCadena);
        subCadena.toCharArray(v, 8 + 1);
        aplicarSubCadena();



        //v = 

    }

    delay(100);
}

void aplicarSubCadena(){
    for(int i = 0; i < 8; i++){
        digitalWrite(leds[i], v[i] - 48);        
    }
}