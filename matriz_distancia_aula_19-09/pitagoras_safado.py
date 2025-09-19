import random

def matriz_distancias(x,y):

    matriz = []
    for i in range(len(x)):
        distancia = []
        for j in range(len(x)):
            d = ((x[j] - x[i])**2 + (y[j] - y[i])**2)**0.5
            distancia.append(d)
        matriz.append(distancia)
    return matriz

lista1 = 5
lista2 = 5


x = [random.randint(1, 10) for _ in range(lista1)]
y = [random.randint(1, 10) for _ in range(lista2)]

print(matriz_distancias(x,y))
