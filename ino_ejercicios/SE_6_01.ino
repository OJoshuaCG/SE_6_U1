// SE - Equipo 6

int leds[8] = {2, 3, 4, 5, 6, 7, 8, 9};
int ledsON[3] = {0, 0 ,0};
int v;

void setup() {
  for(int i = 0; i < 8; i++){
    pinMode(leds[i], OUTPUT);
  }

  randomSeed(analogRead(A0));
  Serial.begin(9600);
}

void loop() {

  digitalWrite(ledsON[0], 0);

  do{
    v = random(8);
  }while(leds[v] == ledsON[0] || leds[v] == ledsON[1] || leds[v] == ledsON[2]);

  ledsON[0] = ledsON[1];
  ledsON[1] = ledsON[2];
  ledsON[2] = leds[v];

  digitalWrite(ledsON[2], 1);  

  delay(1000);
}
