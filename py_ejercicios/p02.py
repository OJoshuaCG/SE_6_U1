import random as rnd

def fo(vector, itemToCount):
    return vector.count(itemToCount)


n = int(input("Ingrese la cantidad de vectores:  "))
m = int(input("Ingrese longitud del vector:      "))
vectores = [[rnd.randint(0,1) for i in range(m)] for i in range(n)]


for i in vectores:
#    print('{}: 1s = {}'.format(i, fo(i, 1)))
    for j in i:
        print('{}, '.format(j), end="")
    print()

'''
3er programa
Aplicar la FO a todos, seleccionar al mejor y enviarlo al arduino
'''