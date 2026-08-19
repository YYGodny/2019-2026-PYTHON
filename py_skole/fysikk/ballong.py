import pygame 


display_surface = pygame.display.set_mode((600, 500))
clock = pygame.time.Clock()

P_METER = 50 #skalering til piksler

g = 9.81 * P_METER #må skalere gravitasjon for at det skal se naturlig ut i piksler
v = 0
a = 0
t = 0
radius = 35 #denne kan endres på for å få ulike resultater
V = (4/3)*3.14*(radius/P_METER)**3
pgass = 0.179
ballong_stoff = 0.05
vekt = ballong_stoff + pgass * V

def ballong(bredde, høyde):
    surface = pygame.Surface((bredde, høyde), pygame.SRCALPHA)
    pygame.draw.ellipse(surface, 'red', (0, 0, bredde, høyde - 10))
    return surface

def L(v, radius_piksler):
    if v > 0:
        p = 1.225 #kg/m^3
        c = 0.47
        #konverterer radius til meter før arealberegning
        radius_meter = radius_piksler/P_METER
        areal = 3.14*(radius_meter**2)
        
        #konverterer hastighet fra piksler/s til meter/s
        v_meter = v/P_METER
        
        #luftmotstand i Newton
        kraft_newton = 0.5*p*(v_meter**2)*c*areal
        
        #gjør kraften om til piksel-skala
        return kraft_newton*P_METER
    return 0

balloon_surface = ballong(radius*2, 100)
balloon_rect = balloon_surface.get_rect(center=(300, 50))

while True:
    dt = clock.tick(60) / 1000
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    print(v)
    display_surface.fill('white')
    
    a = (g*dt - (L(v, radius)/vekt)*dt)*50
    v += a*dt
    balloon_rect.y += v*dt
    t += dt
    
    display_surface.blit(balloon_surface, balloon_rect)

    pygame.display.update()




'''
konklusjonen er at større ballong, gir større akselarasjon.
denne er veldig enkel og samsvarer muligens ikke med virkeligheten
'''
