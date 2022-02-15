int leds[8] = {6, 7, 8, 9, 10, 11, 12, 13};
int ledOn[3] = {-1, -1, -1};

void setup(){
    for(int i = 0; i < 8; i++){
        pinMode(leds[i], OUTPUT);
    }
    
    randomSeed(analogRead(A0));
}

int v, a = 0;
void loop(){         
    again:;
    v = random(8);
    if(repeated())
        goto again;    

    if(ledOn[a] != -1)
        digitalWrite(leds[ledOn[a]], 0); 
     
    ledOn[a] = v;
    digitalWrite(leds[v], 1); 

    a++;
    if(a >= 3)
        a = 0;
    
    delay(1000);    
}

bool repeated(){
    for(int i = 0; i < 3; i++)
        if(ledOn[i] == v)
            return true;

    return false;
}
