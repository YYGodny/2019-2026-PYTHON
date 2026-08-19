#4.87
from pylab import *

def f(x):
    return x**2 + 2*x

x_verdier = linspace(-5, 5, 100)
y_verdier = f(x_verdier)

xlabel('x')
ylabel('f(x)')
axhline(y=0, color='black')
axvline(x=0, color='black')
grid()

plot(x_verdier, y_verdier)
xticks([i for i in range(-5, 6)])
show()
