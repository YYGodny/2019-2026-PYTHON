import matplotlib.pyplot as plt
import numpy as np

V = 25 #m/s
masse = 1400 #kg
L = 0.8*V**2
tørrasfalt = 0.7
våtasfalt = 0.25
N=masse*9.81
Rtørr = tørrasfalt*N
Rvåt = våtasfalt*N

a=(-L-Rvåt)/masse
sekunder = 0
meter = 0
m = []
v = []
s = []
while V > 0:
    meter += V*0.01
    m.append(meter)
    V += a*0.01
    v.append(V)
    L = 0.8*V**2
    a=(-L-Rvåt)/masse
    sekunder += 0.01
    s.append(sekunder)

print(f'den bremset i {meter} meter, i {sekunder} sekunder')
yverdier = np.array(m)
xverdier = np.array(s)
plt.plot(xverdier, yverdier)
plt.show()



