from pylab import *

def f(x):
    return (x**2-3)/(x-9)

x_verdier = linspace(-10, 10, 100)
y_verdier = f(x_verdier)

xlabel('x')
ylabel('f(x)')
axhline(y=0, color='black')
axvline(x=0, color='black')
grid()

plot(x_verdier, y_verdier)
show()
