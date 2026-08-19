import numpy as np
from matplotlib import pyplot as plt

delta_x = 1e-8

def f(x):
    return  2*x**3 + x**2 - 5*x+2

def df(x):
    return ((f(x + delta_x)-f(x))/delta_x)

x_verdier = np.linspace(-5, 5, 100)
y_verdier = f(x_verdier)
dy_verdier = df(x_verdier)

plt.plot(x_verdier, y_verdier)
plt.plot(x_verdier, dy_verdier)
plt.show()

