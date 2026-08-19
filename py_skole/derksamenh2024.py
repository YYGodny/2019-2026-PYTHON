from math import log

dx = 1e-8
a = 3

def f(x):
    return log(a*x)

def fder(x):
    return (f(x+dx)-f(x))/dx

print(fder(2))
