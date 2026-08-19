from math import sin, cos, pi

gamma = 6.67*10**-11
M = 6.3*10**14
R = 4*10**3
g = (gamma*M)/(R**2)
dt = 0.01
t = 0
grader = 45
v0 = 2
vx = v0*cos(grader*(pi/180))
vy = v0*sin(grader*(pi/180))
sx = 0
sy = 0.0000001


while sy > 0:
    sx += vx*dt
    sy += vy*dt
    vy -= (gamma*M)/((R+sy)**2)*dt
    t += dt
    
print(round(sx), round(sy), round(t))
