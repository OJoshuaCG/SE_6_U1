//Maquina,Usuario
int juego[][3] ={        
//   pi  pa  ti
    { 0,  1, -1}, //pi
    {-1,  0,  1}, //pa
    { 1, -1,  0}  //ti
};

void setup() {
    Serial.begin(9600);
    randomSeed(analogRead(A0));
    //Serial.setTimeout(10);
}

String usuario;
int u, m, res;
int edo = 0;
void loop() {
    switch(edo){
        case 0:            
            Serial.println("Ingrese 1=Piedra, 2=Papel, 3=Tijera");
            edo++;
        break;
        case 1: case 5:
            if (Serial.available() > 0) {
                usuario = Serial.readString();
                edo++;
            }
        break;
        case 2: case 6: 
            checkInput();
        break;
        case 3:
            play();
        break;
        case 4:
            Serial.println("Desea jugar de nuevo? 1=SI, 0=NO");
            edo++;
        break;

    }
}

void play(){
    m = random(3);
    print();
    res = juego[m][u];
    if(res == 1)
        Serial.println("Ganaste! :D");    
    else if(res == -1)
        Serial.println("Perdiste :c");
    else
        Serial.println("Empate :o");

    edo++;
}

String getObject(int value){
    if(value == 0)
        return "Piedra"; 
    if(value == 1)
        return "Papel";
    
    return "Tijera";
}   

void print(){
    Serial.println("Usuario: " + getObject(u) 
        + " vs Maquina: " + getObject(m));
}

void checkInput(){
    if(!usuario.equals("")){
        u = usuario.toInt();
        Serial.println(u);
        if(edo == 2){
            if( u > 3 || 1 > u)
                goto back;
        }
        else{
            if(u == 1)
                edo = 0;
            else
                edo++;
            goto end;

        }

        u = u-1;
        edo++;        
    }
    else{
        back:
        Serial.println("Dato invalido");
        edo -= 2;
    }
    end:;    
}

