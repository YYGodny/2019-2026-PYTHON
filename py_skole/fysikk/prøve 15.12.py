import math

m = 2.5
g = 9.81
b = 1.2
r = 0.2
l = 0.4

dt = 0.001
t = 0
s = 0
v = 0
i = 0
while i < 6:
    a = (m*g*math.sin(math.pi/6)- i*l*b)/m
    i = (b*l*v)/r
    v += a*dt
    s += v*dt
    t += dt
    
print(v, t, s, a, i)
