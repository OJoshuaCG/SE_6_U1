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
    limpiar();
    
    if(Serial.available() > 0){
        v = Serial.readString().toInt(); // 0 - 7
        digitalWrite(leds[v], 1);
    }
       
    delay(250);
}

void limpiar(){
    for(int i = 0; i < 8; i++){
        digitalWrite(leds[i], 0);
    }
}

