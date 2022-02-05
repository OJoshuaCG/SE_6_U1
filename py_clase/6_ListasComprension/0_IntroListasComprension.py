# Calcula la sumatoria de todos los numeros enteros comprendidos entre 1 y N (inclusive), y añadelos a una lista

#Si n = 8
'''
numeros = [1, 2, 3, 4, 5, 6, 7, 8]

n = int(input("Ingrese el valor de n: "))
lista = []
for i in range(1, n+1):
    lista.append(i)

print(lista)
'''

#Forma con listas de comprension
n = int(input("Ingrese el valor de n: "))
lista = [i+1 for i in range(n)]
print(lista)