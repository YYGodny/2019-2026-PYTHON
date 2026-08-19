import pygame, time, random

pygame.init()
clock = pygame.time.Clock()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

partikler = []

class Partikkel():
    def __init__(self, x, y):
        #x, y, fartx, farty, liv
        self.x = x
        self.y = y
        self.fart_x = random.randint(-10, 10)
        self.fart_y = random.randint(-20, 2)
        self.liv = random.randint(6, 15)
        self.farge = 255

    def update(self):
        self.x += self.fart_x
        self.y += self.fart_y
        self.fart_y += 0.5
        self.liv -= 0.5
        self.farge -= 7

        if self.y > HEIGHT:
            self.fart_y *=-1
        
        if self.x > WIDTH or self.x < 0:
            self.fart_x *= -1
        
        if self.liv < 1:
            partikler.remove(self)
            del self
        
    def draw(self):
        pygame.draw.circle(screen, (self.farge, 0, 255), (int(self.x), int(self.y)), int(self.liv))

    def oppskytning(self, mx, my):
        y = 0
        x = 0
        xfart = random.randint(-4, 4)
        tall = 200
        for i in range(tall):
            y -= 1
            x += xfart/10
            if tall > (tall/100)*98:
                xfart += xfart/120
                y -= 0.01
            pygame.draw.circle(screen, (self.farge, 0, 255), (int(mx + x), int(my + y)), 3)
        eksplosjon(mx + x, my + y)
        
def eksplosjon(mx, my):
    for i in range(40):
        minPartikkel = Partikkel(mx, my)
        #partikler.append(minPartikkel)
        partikler.insert(0, minPartikkel)


    
running = True
while running:

    screen.fill((0, 0, 0))

    for partikkel in partikler[::-1]:   
        partikkel.update()
        partikkel.draw()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            mx, my = pygame.mouse.get_pos()
            rakket = Partikkel(mx, my)
            rakket.oppskytning(mx, my)
            
    clock.tick(30)
    pygame.display.update()
pygame.quit()


