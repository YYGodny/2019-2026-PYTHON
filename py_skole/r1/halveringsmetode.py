from pylab import *

a = 0.1
b = 2
nøyaktighet = 0.001

def f(x):
    return log(x)+3*x-3

m = (a+b)/2

while abs(f(m)) >= nøyaktighet:
    print(a)
    print(b)
    print(m)
    if f(a)*f(m) < 0:
        b = m
    else:
        a = m
        
    m = (a+b)/2

print("Løsningen er omtrent lik",round(m,4))
