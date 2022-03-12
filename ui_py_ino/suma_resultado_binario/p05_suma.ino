int leds[8] = {2, 3, 4, 5, 6, 7, 8, 9};

void setup() {
    for(int i = 0; i < 8; i++){
        pinMode(leds[i], OUTPUT);
    }
  
    Serial.begin(9600);
    Serial.timeout(10);
}

int cociente, residuo, k=7;
void loop() {
    if(Serial.available() > 0){
        cociente = Serial.readString().toInt(); // 0 - 7
        
        // convertir v en binario para conocer los leds que se deberán prender 
        k=7;
        while(cociente > 0){
            residuo = cociente%2;
            digitalWrite(leds[k--], residuo);
            cociente = cociente/2;
        }

        for(; k>=0; k--){
            digitalWrite(leds[k], 0);
        }        
    }
    delay(100)    
}