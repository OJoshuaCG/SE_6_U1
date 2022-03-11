import random as rnd

def calc_FO(indv):
    return sum(indv)


#  Numero de genes
tot_genes = 10
# Numero de individuos
tot_individuos = 100

poblacion = []
for i in range(tot_individuos):
    poblacion.append([rnd.randint(0,1) for i in range(tot_genes)])

# print("Poblacion Inicial: ")
# for indv in poblacion:
#     print(indv)

padres = []
tot_padres = 50

for i in range(tot_padres):    
    indexPadre1 = rnd.randint(0, tot_individuos-1) # Aleatorio entre 0 y n-1
    indexPadre2 = rnd.randint(0, tot_individuos-1) # Aleatorio entre 0 y n-1

    while(indexPadre1 == indexPadre2):
        indexPadre2 = rnd.randint(0, len(tot_individuos)-1)
    
    tempPadre1 = poblacion[indexPadre1]
    tempPadre2 = poblacion[indexPadre2]

    if(calc_FO(tempPadre1) >= calc_FO(tempPadre2)):
        padres.append(tempPadre1.copy())
    else:
        padres.append(tempPadre2.copy())


print("Padres para cruza: ")
for indrex, padre in enumerate(padres):
    print(index, ". ",padre)


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

    

# Mutacion
probMuta = 0.8
for i in range(len(hijos)):
    hijo = hijos[indexHijo]
    
    for indexGen in range(len(hijo)):
        r = rnd.random()
        if r >= probMuta:
            hijo[indexGen] = 1 if rnd.random() >= 0.5 else 0            
    

### Contamos con poblacion completa
### E hijos