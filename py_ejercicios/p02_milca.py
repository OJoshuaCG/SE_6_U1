def FO (arreglo):
    a = 0
    for i in arreglo:
        a+= i
    return a

import random as rnd

TotalVectores = int(input("Total de Vectores: "))
TamVectores = int(input("Tamaño de Vectores: "))
vectores = []
for i in range(TotalVectores):
    vectores.append([])
    for j in range(TamVectores):
        vectores[i].append(rnd.randrange(0,2))

numv = 0
for k in vectores:
    numv+=1
    print("V", numv, ": ", k, "FO: ", FO(k))