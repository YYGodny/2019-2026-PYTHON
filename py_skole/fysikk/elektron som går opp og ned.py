ke = 8.99E9
Q = 7.0E-9
q = -5.0E-9
d = 4.0E-2
R = 2.0E-2
m = 1.0E-3
v = 0
t = 0
dt = 0.01

s = 0
r0 = 2*R

while s < 2*r0:
    a = (2*ke*R*Q*abs(q))/(m*(d**2+R**2)**(3/2))
    v += a*dt
    s += abs(v*dt)
    R -= v*dt
    t += dt
    
print(t)
