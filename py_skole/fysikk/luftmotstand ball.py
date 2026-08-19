import numpy as np
import pygame

#lager en liste med tusen tidsverdier fra 0 til 3 sekunder. lengden av hvert tidsted vi dt

n = 1000
T = 3 #sek
t = np.linspace(0, T, n)
dt = T/n

#tomme lister for s, v og a til å plotte dataene

s = np.zeros(n)
v = np.zeros(n)
a = np.zeros(n)

#definerer konstanter og startverdier

m = 0.200 #ballens masse i kg
g = 9.81 #tyngdeakselerasjon
k = 0.01 #n/(m/s)**2
v[0] = 10 #startfart m/s

#bestemmer kreftene og beregner akselerasjon med n2 for hvert tidssteg
#antar konstant fart og akselerasjon i hvert tidsskritt, og bruker dette til å regne ut ny fart, posisjon og akselerasjon
'''

for i in range(n-1):
    G = -m*g
    L = -k*v[i]*abs(v[i])
    F_sum = L+ G
    a[i] = F_sum/m
    v[i+1] = v[i] + a[i]*dt
    s[i+1] = s[i] + v[i+1]*dt
'''

pygame.init()

screen_res = (1000, 600)
screen = pygame.display.set_mode(screen_res)
red = (255, 0, 0)
black = (0, 0, 0)
ball = pygame.draw.circle(surface = screen, color = black, center=[300, 0], radius = 40)

x=1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    if x == 1:
        for i in range(n-1):
            screen.fill(black)
            pygame.draw.circle(surface=screen, color=red,
                               center=ball.center, radius=40)
            G = -m*g
            L = -k*v[i]*abs(v[i])
            F_sum = L+ G
            a[i] = F_sum/m
            v[i+1] = v[i] + a[i]*dt
            s[i+1] = s[i] + v[i+1]*dt
            ball = ball.move(0, s[i])
                
            pygame.display.flip()
        x= 2
