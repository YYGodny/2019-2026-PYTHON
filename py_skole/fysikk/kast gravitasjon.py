import math

def finne_strekning(u):
    gamma = 6.67E-11
    M = 7.34e22#5.97E24
    R= 1.74e6#6.37E6
    v = 2000
    vy = math.sin(u)*v
    vx = math.cos(u)*v
    r=R+0.1
    t=0
    dt=0.1
    s = 0

    maksh = 0

    while r > R:
        a=-gamma*M/r**2
        r += vy*dt
        vy += a*dt
        s += vx*dt
        t += dt
        if vy < 0 and r > maksh:
            maksh = r
            
    return int(s)

u = 0
maks_strekning = 0
maks_u = 0

while u < math.pi*2:
        if maks_strekning < finne_strekning(u):
            maks_strekning = finne_strekning(u)
            maks_u = u
        u += 0.01
        
print(maks_strekning, maks_u*(180/math.pi))
