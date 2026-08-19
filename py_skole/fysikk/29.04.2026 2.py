from math import sqrt, pi
m = 1.67e-27
c = 3e8
R = 4300
q = 1.6e-19
dU = 15e6 #det står 5mV i oppgaven

v = 0.1*c
dt = 0.00001
t = (2*pi*R)/v

t_tot = 0

while v < 0.995*c:
    if t <= 0:
        v += sqrt((2*dU*q)/m)
        t = (2*pi*R)/v
    t -= dt
    t_tot += dt

print(t_tot)
    
