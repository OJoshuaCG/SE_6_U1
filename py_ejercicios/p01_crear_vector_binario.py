'''
18 / 01 / 2022
1. Generar un arreglo de tamaño n (n >= 2)
2. Cada posicion del arreglo la van a rellenar con un 0 o un 1 random
3. Generar un metodo de nombre FO que permitira obtener el conteo de todos los 1s en el arreglo
4. aplicar el metodo al arreglo generado para el valor de n ingresado por el usuario
5. Desplegar el resultado obtenido por el metodo FO
'''

#import random as rnd

def fo(vector, itemToCount):
    return vector.count(itemToCount)


n = int(input("Ingrese longitud del vector:  "))

vector = [rnd.randint(0,1)      for i in range(n)]
          # Valor a asignar     Ciclo, que nos permite relizar
          #                     'n' veces la asignacion

print(vector)
print(fo(vector, 1))


