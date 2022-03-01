import random as rnd

def calc_FO(indv):
    return sum(indv)


tot_genes = 10          # Numero de genes 10
tot_individuos = 100    # Numero de individuos 100
tot_padres = 50         # Numero de padres 50
num_gener = 0           # Numero de generacion

# Lista en donde almacenaremos TODA la poblacion
poblacion = []
# Lista de ayuda, donde almacenaremos la generacion
generacion = [] 

# Creamos un 'individuo' con 'tot_genes' caracteristicas aleatorias
# entre un rango de 0 y 1, ademas de sumar sus caracteristicas
# para esto hacerlo una lista y añadirlo a la 'generacion'
for i in range(tot_individuos):
    individuo = [rnd.randint(0,1) for i in range(tot_genes)]
    generacion.append([individuo, calc_FO(individuo)])

poblacion.append(generacion) 

# 'seleccion' (ganadores) de los padres o ganadores del torneo binario
seleccion = []

# ----------------------------------------------------
# Torneo Binario
# ----------------------------------------------------
for i in range(tot_padres):    
    indexPadre1 = rnd.randint(0, tot_individuos-1) # Indice aleatorio entre 0 y n-1
    indexPadre2 = rnd.randint(0, tot_individuos-1) # Indice aleatorio entre 0 y n-1

    # Mientras sean repetidos, buscaremos otro indice
    while(indexPadre1 == indexPadre2):
        indexPadre2 = rnd.randint(0, tot_individuos-1)


    if(poblacion[num_gener][indexPadre1][0] 
        >=
        poblacion[num_gener][indexPadre2][0]):
    
    #if(calc_FO(tempPadre1) >= calc_FO(tempPadre2)):
        seleccion.append(poblacion[num_gener][indexPadre1].copy())
    else:
        seleccion.append(poblacion[num_gener][indexPadre1].copy())



# print("Padres para cruza: ")
# for index, padre in enumerate(seleccion):
#     print(index, ". ",padre)


hijos = []
for i in range(0, tot_padres, 2):
    tempPadre1 = padres[i]
    tempPadre2 = padres[i+1]

    #Generar un aleatorio
    puntoCruza = rnd.randint(0, tot_genes-1)

    hijo1 = []
    hijo2 = []

    puntoCruza += 1 # +1 -> puntoCruza incluyente

    hijo1 = tempPadre1[:puntoCruza] + tempPadre2[puntoCruza:]
    hijo2 = tempPadre2[:puntoCruza] + tempPadre1[puntoCruza:]

    hijos.append(hijo1)
    hijos.append(hijo2)

    
'''
# Mutacion
probMuta = 0.8
for i in range(len(hijos)):
    hijo = hijos[indexHijo]
    
    for indexGen in range(len(hijo)):
        r = rnd.random()
        if r >= probMuta:
            hijo[indexGen] = 1 if rnd.random() >= 0.5 else 0            
'''

### Contamos con poblacion completa
### E hijos