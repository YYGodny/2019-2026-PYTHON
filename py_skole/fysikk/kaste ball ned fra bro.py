import numpy as np
import matplotlib.pyplot as plt

# Vertikal ball-SLIPP med luftmotstand

# Funksjon for Luftmotstand
def L(v,k):
    return -k * v * np.abs(v)

# Konstanter. Positiv retning OPP
m = 0.03115     # kg
g = -9.81   # m/s**2
v0 = 0.0   # m/s
s0 = 10.6    # m
t0 = 0.0  # s
dt = 0.1    # s  Tidsdelta
k =  0.006    # N/(m**2/s**2)    friksjonskonstant luft

# Variabler og initialisering
t = [t0]
s = [s0]
v = [v0]
a = [(m*g + L(v[-1], k))/m]

while s[-1] >= 0:
    Fsum = m*g + L(v[-1], k)
    a1 = Fsum/m
    v1 = v[-1] + a1*dt
    s1 = s[-1] + v1*dt
    t1 = t[-1] + dt
    # Sparer på data for plotting
    s.append(s1)
    v.append(v1)
    a.append(a1)
    t.append(t1)

print( f"Falltiden ble {t[-1]}"  )

plt.title("Fart (+ OPP)")
plt.plot(t, v)
plt.show()
plt.title("Posisjon (+ OPP)")
plt.plot(t, s)
plt.show()
plt.title("Akselerasjon (+ OPP)")
plt.plot(t, a)
plt.show()

