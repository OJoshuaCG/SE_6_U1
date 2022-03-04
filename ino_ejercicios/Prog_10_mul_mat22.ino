#include <stdio.h>

void setup() {
    Serial.begin(9600);
    Serial.setTimeout(10);
}

int A[2][2];
int B[2][2];
int C[2][2];

void loop() {
    
}


void printMat(int x[][2]){
    Serial.println(String(x[0][0]) + "  " + String(x[0][1]));
    Serial.println(String(x[1][0]) + "  " + String(x[1][1]));
}

char row[39];
void printMul(){
    sprintf(row, "|%4i,%4i| v |%4i,%4i| _ |%4i,%4i|", A[0][0], A[0][1], B[0][0], B[0][1], C[0][0], C[0][1]);
    Serial.println(row);
    sprintf(row, "|%4i,%4i| ^ |%4i,%4i| - |%4i,%4i|", A[1][0], A[1][1], B[1][0], B[1][1], C[1][0], C[1][1]);
    Serial.println(row);
}


void multiply(){
    C[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0];
    C[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1];
    C[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0];
    C[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1];
    
    printMul();
}   