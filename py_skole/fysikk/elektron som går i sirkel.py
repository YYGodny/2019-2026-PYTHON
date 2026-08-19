from math import pi
e = 1.602E-19
m = 9.109E-31
v = 8.0E6
t = 0
B = 3.20E-3
dB = 0.20E-3

r = (m*v)/(e*B)

for n in range(15):
    v = (e*B*r)/m
    r = (m*v)/(e*B)
    t += (2*pi*r)/v
    B = B + dB
    
print(t)
