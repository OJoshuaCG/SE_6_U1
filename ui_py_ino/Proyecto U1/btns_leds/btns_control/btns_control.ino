
int botones [6] = {3,4,5,6,7,8};

void setup() {
    for(int i = 0; i < 5; i++){
        pinMode(botones[i], INPUT_PULLUP);
    }
    Serial.begin(9600);
    Serial.setTimeout(200);
}

int edosBtns [6]= {0, 0, 0, 0, 0, 0};

void loop() {
    String cadena = "";
    
    for(int i = 0; i < 6; i++){
        edosBtns[i] = digitalRead(botones[i]);
        if (!edosBtns[i] == 1)
          cadena = String(i);
    }
    
    cadena += "\n";    
    Serial.println(cadena);

    delay(100);
}
