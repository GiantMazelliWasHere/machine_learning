import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calcula(x, y):
    x = np.array(x)
    y = np.array(y)
    x_bar = np.mean(x)
    y_bar = np.mean(y)
    m = np.dot(x - x_bar, y - y_bar) / np.dot((x - x_bar, x - x_bar))
    print(m)
    b = y_bar - m * x_bar
    print(b)
    plt.plot( x, m * x + b)
    plt.plot( x, y)
    plt.show()

data = pd.read_excel("data.xlsx")

print(data)
x, y = data['x'], data['y']
calcula(x, y)