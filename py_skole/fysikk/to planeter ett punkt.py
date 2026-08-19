gamma = 6.67e-11
M = 2.6e26
m = 1.50e23
v = 0
t = 0
r = 1.2*10**5
s = 1*10**7
d = 5.50 * 10**7
R = 2.30 * 10**7

dt = 0.01
while s > r:
    a = ((gamma*M)/((R+d)**2))+((gamma*m)/(s**2))
    v += a*dt
    s -= v*dt
    d -= v*dt
    t += dt

print(round(t))
    
    
