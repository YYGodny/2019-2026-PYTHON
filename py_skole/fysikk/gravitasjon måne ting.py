gamma = 6.67*10**(-11)
M = 7.35*10**22
r = 1737*10**3
v = 1.44*10**3
t = 0
dt = 0.001

s = r + 900*10**3

while s > r:
    a = (gamma*M)/(s**2)
    v += a*dt
    s -= v*dt
    t += dt
    
print(t)
