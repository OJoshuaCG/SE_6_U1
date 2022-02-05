//2. Volumen de un cuadrilátero dadas las medidas de cada uno de sus lados

void setup() {
    Serial.begin(9600);
    Serial.timeout(10);
}

int x, y, h, v, res;
String valor, msg;
int edo = 0;
void loop() {
    switch(edo){
        case 0: case 3: case 6:        
            if(estado == 0)
                msg = "A";
            else if(estado == 3)
                msg = "B";
            else(estado == 6)
                msg = "H";
            
            Serial.println("Ingrese lado " + msg + ": ");
            edo++;
        break;
        case 1: case 4: case 7: case 11:           
            if(Serial.available()>0){
                valor = Serial.readString();
                edo++;
            }
        break;
        case 2: case 5: case 8: case 12:
            if(!valor.equals("")){
                v = valor.toInt();
                Serial.println(v);
                if(v == 0)                  
                    goto back;

                if(edo == 2)
                    x = v;
                else if(edo == 5)
                    y = v;
                else if(edo == 8)
                    h = v;
                else
                    if(v == 1)
                        edo = 0;
                    else
                        edo++;
                    break;

                edo++;
            }
            else{
                back:
                Serial.println("Dato invalido");
                edo -= 2;
            }
        break;
        case 9:
            res = x * y * h;
            Serial.println("Resultado: "+String(res));
            edo++;
        break;
        case 10:
            Serial.println("Deseas realizarlo de nuevo? 1 = Si | 0 = No");
            edo++;
        break;
    }
}