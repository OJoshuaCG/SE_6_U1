#archivo = open("6_ListasComprension/Archivo.csv")
archivo = open("Archivo.csv")

contenidoArchivo = archivo.readlines()
#print(contenidoArchivo)
print(contenidoArchivo)

#archivoProcesado = [i.split(",") for i in contenidoArchivo]
archivoProcesado = [list(map(int,i.split(","))) for i in contenidoArchivo]

print("Archivo procesado: ")
for i in archivoProcesado:
    print(i)

instancia = [list(map(int, i)) for i in archivoProcesado]
#print(instancia)


# Tarea: Crear una interfaz grafica que lea a las preferencias de los usuarios, y con base en un boton para cada usuario les aplique en arduino
