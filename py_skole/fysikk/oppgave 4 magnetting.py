t = 0
dt = 0.0001
g = 9.81
k = 4.878
s = 0
v = 0
b = 0.5
r = 0.041
l = 0.2

while s < 1.2:
    s += v*dt
    a = g - k*v
    v += a*dt
    t += dt
    i = (v*b*l)/r

print(i)
print(s,v)


##annen oppgave
from math import sqrt
q = 1.60e-19
m = 1.6726e-27
b = 0.045
u = 500
v = 0

n = 0
while v < (3*10**8)*0.1:
    v = sqrt(v**2+2*q*u/m)
    r = (m*v)/(q*b)
    n += 1
print(v, r, n)
