import pygame

class person:
    def __init__(self):
        self.x = 0
        self.y = 0
        
    def update(self):
        pygame.draw.rect(screen, (0, 0, 255), [50, 50, 50, 50], 0)

p1 = person()


pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('spill med kart')


playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                p1.y -= 1
            if event.key == pygame.K_a:
                p1.x -= 1
            if event.key == pygame.K_s:
                p1.y += 1
            if event.key == pygame.K_d:
                p1.x += 1
                
    screen.fill((255, 255, 255))
    p1.update()
    
    pygame.display.update()
    
pygame.quit()
