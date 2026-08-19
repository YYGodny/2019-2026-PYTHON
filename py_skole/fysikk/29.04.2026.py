G = 6.67e-11
M = 5.97e24
R = 6.37e6
m = 9000
k = 0
v = 420
S = R + 8000
dt = 0.001

v1 = 8

while round(v,1) > v1:
    v = 420
    S = R + 8000
    while S > R:
        a = (G*M)/S**2 - (k*v**2)/m
        v += a*dt
        S -= v*dt
    k += 50
print(v, k)
