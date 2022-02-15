def checkPar(n):
    if n%2==0:
        return "par"
    else:
        return "impar"


lista = [10, 15, 20, 45]

print(list(zip(lista, list(map(checkPar, lista)))))
print("xdd")



#for i in lista:
#    checkPar(i)
    # if i%2==0:
    #     print("par")
    # else:
    #     print("impar")


