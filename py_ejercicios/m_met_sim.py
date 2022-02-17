'''
Instancia
Preferencias de usuario
usuario -> vector de caracteristicas
Aplicar las metricas
'''


def Manhattan(A, B):
    d = sum([
        abs(A[i]-B[i])
        for i in range(len(A)) 
    ])    
    return d


def Euclidiana(A, B):
    d = sum([
        (A[i]-B[i])**2
        for i in range(len(A))
    ])**0.5
    return d


def EuclidianaProm(A, B):
    d = (sum([
        (A[i]-B[i])**2
        for i in range(len(A))
    ])/len(A))**0.5
    return d


def DifCarProm(A, B):
    d = Manhattan(A, B)/len(A)
    return d


def Canberra(A, B):
    d = sum([
        abs(A[i]-B[i])/
        (abs(A[i])+ abs(B[i]))         
        for i in range(len(A))        
        ])    
    return d


def BrayCurtis(A, B):
    num = sum([
        abs(A[i]-B[i]) 
        for i in range(len(A))
        ])
    den = 2 + sum([
        A[i]+B[i]
        ])
    return(num/den)


def Coseno(A, B):
    num = sum([
        A[i]*B[i]
        for i in range(len(A))
    ])
    den = xDos(A) * xDos(B)
    return(num/den)
    

def Orloci(A, B):
    d = (2-2*Coseno(A, B))**0.5
    return d
    

def xDos(A):
    x = sum([
        i**2 
        for i in A
    ])**0.5
    return x


A = [1, 2, 3, 4, 5]
B = [7, 9, 4, 6, 3]

print(Manhattan(A, B))
print(Euclidiana(A, B))
print(EuclidianaProm(A, B))
print(DifCarProm(A, B))
print(Canberra(A, B))


