#include <iostream>
using namespace std;

int A[][2] = {{-5, 3}, {4, 7}};
int B[][2] = {{9, 0}, {2, -5}}; 
int C[2][2];

void printMat(){
    for(int i = 0; i < 2; i++){
        for(int j = 0; j < 2; j++){
            cout << "i= " << i << " | j= " << j << "  :  " << C[i][j] << endl;
        }
    }
}

void multiply(){
    C[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0];
    C[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1];
    C[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0];
    C[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1];
    printMat();
}



int main(){
    multiply();
   

    return 0;
}

