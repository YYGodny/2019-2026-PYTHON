import pygame, random, sys, time


def won():
    if player1.dead == True:
        won_surface = game_font.render('PLAYER2 WON!', True, (255, 255, 255))
        won_rect = won_surface.get_rect(center = (313, 192))
        screen.blit(won_surface, won_rect)
    elif player2.dead == True:
        won_surface = game_font.render('PLAYER1 WON!', True, (255, 255, 255))
        won_rect = won_surface.get_rect(center = (313, 192))
        screen.blit(won_surface, won_rect)

framesy = 0        
def menu(x):
    global framesy
    menu_surface = pygame.image.load(r'bilder/menu.png').convert()
    screen.blit(menu_surface, (470, 315))
    menu2_surface = pygame.transform.scale(pygame.image.load(r'bilder/menu2.png'), (200, 383)).convert()
    frame_surface1 = pygame.image.load(r'bilder/character frame.png')
    frame_surface1_rect = frame_surface1.get_rect(topleft = (0, 0 + framesy))
    if x == True:        
        screen.blit(menu2_surface, (0, 0))
        screen.blit(frame_surface1, frame_surface1_rect)
    if x == False:
        screen.blit(bg_surface, (0, 0), pygame.Rect(0, 0, 200, 383))

inside = False

def check_inside():
    global inside
    if player1.moo_rect.centerx > player2.moo_rect.midleft[0] and player1.moo_rect.centerx < player2.moo_rect.midright[0]:
        if player1.moo_rect.centery == player2.moo_rect.centery:
            return True
    else:
        return False
    
def check_collision():
    if player1.moo_rect.colliderect(player2.moo_rect) and player1.moo_rect.centery < player2.moo_rect.centery:
        player2.lose_health()
    elif player2.moo_rect.colliderect(player1.moo_rect) and player2.moo_rect.centery < player1.moo_rect.centery:
        player1.lose_health()

        
pygame.init()
screen = pygame.display.set_mode((626, 383))
clock = pygame.time.Clock()
pygame.display.set_caption('JEAD')
game_font = pygame.font.Font(r'HackbotFreeTrial-8MgA2.otf', 30)
game_font2 = pygame.font.Font(r'HackbotFreeTrial-8MgA2.otf', 20)

bg_surface = pygame.image.load(r'bilder/jeadbackground.jpg').convert()

class moo(pygame.sprite.Sprite):
    def __init__(self, p1_eller_p2):
        super().__init__()
        self.p1_eller_p2 = p1_eller_p2
        if p1_eller_p2 == 'p1':
            self.image = pygame.transform.scale2x(pygame.image.load(r'bilder/MOO.png')).convert_alpha()
            self.moox = 360
            self.mooy = 270

            self.dead = False
            self.mistethealth2 = 0
            self.mistethealth = 6
            self.har_health = 100
            self.hbf_surface = pygame.transform.scale(pygame.image.load(r'bilder\full health.png'), (self.har_health, 23)).convert_alpha()
            self.hbn_surface = pygame.transform.scale(pygame.image.load(r'bilder\null health.png'), (112, 23)).convert_alpha()
            self.hbh_surface = pygame.transform.scale(pygame.image.load(r'bilder\heart.png'), (23, 23)).convert_alpha()

            self.playername = game_font2.render('PLAYER1', True, (255, 255, 255))
            
        else:
            self.image = pygame.transform.scale2x(pygame.image.load(r'bilder/MOO2.png')).convert_alpha()
            self.moox = 240
            self.mooy = 270

            self.dead = False
            self.mistethealth2 = 0
            self.mistethealth = 6
            self.har_health = 100
            self.hbf_surface = pygame.transform.scale(pygame.image.load(r'bilder\full health.png'), (self.har_health, 23)).convert_alpha()
            self.hbn_surface = pygame.transform.scale(pygame.image.load(r'bilder\null health.png'), (112, 23)).convert_alpha()
            self.hbh_surface = pygame.transform.scale(pygame.image.load(r'bilder\heart.png'), (23, 23)).convert_alpha()

            self.playername = game_font2.render('PLAYER2', True, (255, 255, 255))
            
    def update(self):
        self.hbf_rect = self.hbf_surface.get_rect()
        self.hbn_rect = self.hbn_surface.get_rect()
        self.hbh_rect = self.hbh_surface.get_rect()
        self.moo_rect = self.image.get_rect(center = (self.moox, self.mooy))
        self.playername_rect = self.playername.get_rect(centerx = (self.moo_rect.centerx))
        screen.blit(self.image, self.moo_rect)
        screen.blit(self.hbn_surface, (self.moo_rect.midbottom[0] - self.hbn_rect.center[0], self.moo_rect.midbottom[1]))
        screen.blit(self.hbf_surface, (self.moo_rect.midbottom[0] - self.hbf_rect.center[0] + self.mistethealth2 + 4, self.moo_rect.midbottom[1]))
        screen.blit(self.hbh_surface, (self.moo_rect.midbottom[0] - self.hbn_rect.center[0], self.moo_rect.midbottom[1]))
        screen.blit(self.playername, (self.playername_rect[0], self.moo_rect.midtop[1] - 15))
        
    def lose_health(self):
        if self.har_health >= 7:
            self.mistethealth2 -= 3
            self.har_health -= self.mistethealth
            self.hbf_surface = pygame.transform.scale(pygame.image.load(r'bilder\full health.png'), (self.har_health, 23)).convert_alpha()
            self.hbf_rect = self.hbf_surface.get_rect()
        else:
            self.dead = True

    def rotate(self, way):
        if way == 'right':
            self.image = pygame.transform.scale2x(pygame.image.load(r'bilder/MOO2.png')).convert_alpha()
        elif way == 'left':
            self.image = pygame.transform.scale2x(pygame.image.load(r'bilder/MOO.png')).convert_alpha()

    def reset(self):
        if self.p1_eller_p2 == 'p1':
            self.image = pygame.transform.scale2x(pygame.image.load(r'bilder/MOO.png')).convert_alpha()
            self.moox = 360
            self.mooy = 270

            self.dead = False
            self.mistethealth2 = 0
            self.mistethealth = 6
            self.har_health = 100
            self.hbf_surface = pygame.transform.scale(pygame.image.load(r'bilder\full health.png'), (self.har_health, 23)).convert_alpha()
            self.hbn_surface = pygame.transform.scale(pygame.image.load(r'bilder\null health.png'), (112, 23)).convert_alpha()
            self.hbh_surface = pygame.transform.scale(pygame.image.load(r'bilder\heart.png'), (23, 23)).convert_alpha()

            self.playername = game_font2.render('PLAYER1', True, (255, 255, 255))
            
        else:
            self.image = pygame.transform.scale2x(pygame.image.load(r'bilder/MOO2.png')).convert_alpha()
            self.moox = 240
            self.mooy = 270

            self.dead = False
            self.mistethealth2 = 0
            self.mistethealth = 6
            self.har_health = 100
            self.hbf_surface = pygame.transform.scale(pygame.image.load(r'bilder\full health.png'), (self.har_health, 23)).convert_alpha()
            self.hbn_surface = pygame.transform.scale(pygame.image.load(r'bilder\null health.png'), (112, 23)).convert_alpha()
            self.hbh_surface = pygame.transform.scale(pygame.image.load(r'bilder\heart.png'), (23, 23)).convert_alpha()

            self.playername = game_font2.render('PLAYER2', True, (255, 255, 255))

        
player2 = moo('p2')
player1 = moo('p1')

jumpcount = 10
jumpcount2 = 10
jump = False
jump2 = False
a = False

run = True
gaming = True

menu2 = False
ga = False
c = 0
b = 1

while gaming:
    
    mx, my = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and run == False:
                if mx < 607 and mx > 470 and my < 364 and my > 315:
                    menu2 = not menu2
                    menu(menu2)
                elif mx < 200:
                    continue
                else:
                    player1.reset()
                    player2.reset()
                    c = 0
                    b = 0
                    framesy = 0
                    run = True
            #scroll up
            elif event.button == 4 and run == False and mx < 200 and menu2 == True:
                framesy -= 8
                menu(True)
            #scroll down
            elif event.button == 5 and run == False and mx < 200 and menu2 == True:
                framesy += 8
                menu(True)
                
                
    keys = pygame.key.get_pressed()
    
    if run:
        if player1.dead == False and player2.dead == False:
            #player 1
            if keys[pygame.K_w]:
                pass
            if keys[pygame.K_a]:
                if player1.moo_rect.left >= 0:
                    player1.moox -= 5
                    player1.rotate('left')
            if keys[pygame.K_d]:
                if player1.moo_rect.right <= 636:
                    player1.moox += 5
                    player1.rotate('right')
            if not jump:
                if keys[pygame.K_SPACE]:
                    jump = True
                    a = check_inside()
            else:
                if jumpcount >= -10:
                    neg = 1
                    if jumpcount < 0:
                        neg = -1
                    player1.mooy -= (jumpcount ** 2) * 0.5 * neg
                    jumpcount -= 1
                else:
                    jump = False
                    jumpcount = 10

            #player 2
            if keys[pygame.K_w]:
                pass
            if keys[pygame.K_LEFT]:
                if player2.moo_rect.left >= 0:
                    player2.moox -= 5
                    player2.rotate('left')
            if keys[pygame.K_RIGHT]:
                if player2.moo_rect.right <= 636:
                    player2.moox += 5
                    player2.rotate('right')
            if not jump2:
                if keys[pygame.K_UP]:
                    jump2 = True
                    a = check_inside()
            else:
                if jumpcount2 >= -10:
                    neg2 = 1
                    if jumpcount2 < 0:
                        neg2 = -1
                    player2.mooy -= (jumpcount2 ** 2) * 0.5 * neg2
                    jumpcount2 -= 1
                else:
                    jump2 = False
                    jumpcount2 = 10
                    
            screen.blit(bg_surface, (0, 0))
            player1.update()
            player2.update()
            if a == False:
                check_collision()
            if player1.mooy > 270 or player2.mooy > 270:
                player1.mooy = 270
                player2.mooy = 270
        elif player1.dead == True or player2.dead == True:
            run = False
            ga = True
            
    if c > 40:
            ga = False

    if ga:
        if ga == True and player1.dead == True or player2.dead == True:
            player1.mooy += b
            player2.mooy += b
            screen.blit(bg_surface, (0, 0))
            player1.update()
            player2.update()
            won()
            menu('1')
            b += 1
            c += 1

    pygame.display.update()
    clock.tick(60)
