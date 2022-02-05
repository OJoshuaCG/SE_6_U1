int leds[8] = {6, 7, 8, 9, 10, 11, 12, 13};

void setup(){
    for(int i = 0; i < 8; i++){
        pinMode(leds[i], OUTPUT);
    }    

    Serial.begin(9600);
    Serial.setTimeout(250);
}


int v;
void loop(){
    Serial.println("Conexion Realizada");
    delay(250);
}
