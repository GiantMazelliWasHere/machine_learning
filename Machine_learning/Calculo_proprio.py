import numpy as np
import pandas as pd

data = pd.read_excel("data.xlsx")

lista_x = data["x"]
lista_y = data["y"]

def calculo(lista_x, lista_y):

    media_x = np.mean(lista_x)
    media_y = np.mean(lista_y)


    numerador = 0
    denominador = 0


    for x, y in zip(lista_x, lista_y):
        numerador += (x - media_x) * (y - media_y)
        denominador += (x - media_x) ** 2


    if denominador == 0:
        return 0
    else:
        m = numerador / denominador
        return m


declive = calculo(lista_x, lista_y)
print(f"O declive (m) calculado é: {declive}")