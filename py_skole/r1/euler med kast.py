'''
gamma=6.63*10**(-11)
M=5.97*10**24
R=6.37*10**6
r=R+0.001
v=1500
t=0
dt=0.1
a=0

while r>R:
    a=-gamma*M/r**2
    v=v+a*dt
    r=r+v*dt
    t=t+dt
    
    
print(a,v,t,r-R)
'''

gamma=6.63*10**(-11)
M=5.97*10**24
R=6.37*10**6
r=R+0.001
v=1500
t=0
dt=0.1
a=0

while v>0:
    a=-gamma*M/r**2
    v=v+a*dt
    r=r+v*dt
    t=t+dt
    
    
print(a,v,t,r-R)
