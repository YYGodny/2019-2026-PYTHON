from math import sin, cos, pi

g = 9.81
dt = 0.001
t = 1.2 #tiden vi målte opp og ned
mål = 1 #meter


def finn_startfart(tid):
    t = 0
    v0 = 0
    while tid/2 > t:
        v0 += g*dt
        t += dt
    return v0

def skyt(v0, mål, grader):
    sx = 0
    sy = 0.000001
    vx = v0*cos(grader)
    vy = v0*sin(grader)
    t = 0
    while sy > 0:
        sx += vx*dt
        sy += -0.5*g*dt**2 + vy*dt
        vy += -g*dt
        t += dt
        
    #vi returner om sx er innenfor 0.005 meter av målet, og grader, og tiden
    return (sx < mål + 0.005 and sx > mål - 0.005, round(grader*(180/pi), 1), round(t, 2))


grader = 0
grader_dt = 0.001
resultater = []

while grader < pi*2:
    resultat = skyt(round(finn_startfart(t), 2), mål, grader)
    if resultat[0] == True:
        resultater.append(resultat)
    grader += grader_dt

print(resultater)
    
        
