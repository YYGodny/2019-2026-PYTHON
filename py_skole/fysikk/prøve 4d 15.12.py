import matplotlib.pyplot as plt
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
iy = []
tx = []

while s < 1.2+3*l:#1.2meter pluss 3L
    a = (m*g*math.sin(math.pi/6)- i*l*b)/m
    if s > 1.2:#går inn i magnetfeltet etter 1.2meter
        i = (b*l*v)/r   
    v += a*dt
    s += v*dt
    t += dt
    tx.append(t)
    iy.append(i)

iy = map(lambda x: -x, iy)
plt.plot(tx, iy)
plt.legend('I')
plt.xlabel('tid')
plt.ylabel('strøm')
plt.show()

