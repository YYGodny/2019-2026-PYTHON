from math import sin, cos, radians

gamma = 6.67 * 10**-11
r = 1737 * 10**3
v0 = 1000
vx = v0*cos(radians(60))
vy = v0*sin(radians(60))
M = 7.35 * 10**22
t = 0
dt = 0.001
h = 0
s = 0


while h >= 0:
    a = (gamma*M)/((r+h)**2) #denne tar hensyn til høyden også - derfor (r+h)**2
    vy -= a*dt
    h += vy*dt
    s += vx*dt
    t += dt

print(t, s)
    
