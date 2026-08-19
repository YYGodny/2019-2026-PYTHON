import pygame
import os
import random

pygame.init()

screen = pygame.display.set_mode((600, 650))
pygame.display.set_caption('Tetris')

bildedir = r'C:\Users\fipha001\OneDrive - Osloskolen\py\py_skole\pyskolepygame\tetis\bilder'
b = [pygame.image.load(f'{bildedir}//{i}').convert_alpha() for i in os.listdir(bildedir) if i.endswith('.png')]
b = [pygame.transform.scale(i, (i.get_rect().width/1.39, i.get_rect().height/1.39)) for i in b]


class figurer(pygame.sprite.Sprite):
    def __init__(self, blokk):
        super().__init__()
        self.image = b[blokk].convert_alpha()
        self.rect = self.image.get_rect(center = (300, -20))
                
    def update(self):
        pass


GRAVITY_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(GRAVITY_EVENT, 50)
        
game = True
currentb = figurer(1)
currentbgroup = pygame.sprite.Group()
currentbgroup.add(currentb)

blocks = pygame.sprite.Group()

mscreenw = 300
mscreenh = 610
mscreenx = 200
mscreeny = 20

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            game = False
        if event.type == GRAVITY_EVENT:
            currentb.rect.y += 1
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                currentb.image = pygame.transform.rotate(currentb.image, 90)
                currentb.rect = currentb.image.get_rect(center=currentb.rect.center)
                
    pressedk = pygame.key.get_pressed()
    
    if currentb.rect.left > mscreenx:
        if pressedk[pygame.K_a] or pressedk[pygame.K_LEFT]:
                currentb.rect.x -= 1
    if currentb.rect.right < mscreenx+mscreenw:
        if pressedk[pygame.K_d] or pressedk[pygame.K_RIGHT]:
            currentb.rect.x += 1
        
    if pressedk[pygame.K_s] or pressedk[pygame.K_DOWN]:
        currentb.rect.y += 1

    screen.fill((0, 0, 0))
    screen.fill((155, 155, 155), (mscreenx, mscreeny, mscreenw, mscreenh))
    
    if currentb.rect.bottom >= mscreeny+mscreenh or pygame.sprite.spritecollide(currentb, blocks, False):
        blocks.add(currentb)
        currentbgroup.remove(currentb)
        currentb = figurer(random.randint(0, len(b)-1))
        currentbgroup.add(currentb)
        
    blocks.update()
    blocks.draw(screen)
    currentbgroup.update()
    currentbgroup.draw(screen)

    pygame.display.flip()




