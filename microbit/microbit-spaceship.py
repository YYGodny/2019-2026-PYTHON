import serial
import random
import time
import pygame
import threading
import sys


#serial
ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM5'
ser.open()

microy = 0
microx = 0

def microbit_input():
    global microbitdata, microx, microy
    while True:
        microbitdata = str(ser.readline())
        microbitdata = microbitdata.split("'")[1]
        microbitdata = microbitdata.replace(' ', '')
        microbitdata = microbitdata.replace('\\r', '')
        microbitdata = microbitdata.replace('\\n', '')
        if len(microbitdata) >= 7:
            continue
        try:
            if microbitdata[0] == 'x' and 'y' not in microbitdata:
                xv = microbitdata.replace('x:', '')
                if xv != '':
                    microx = microbitdata[2:]
            if microbitdata[0] == 'y' and 'x' not in microbitdata:
                yv = microbitdata.replace('y:', '')
                if yv != '':
                    microy = microbitdata[2:]
        except:
            pass

th1 = threading.Thread(target=microbit_input, daemon = True)
th1.start()


#pygame
class Player:
    def __init__(self):
        self.x = screen_width/2 - 15
        self.y = screen_height-screen_height/4
        self.player1 = pygame.transform.scale(pygame.image.load('space_ship.png').convert_alpha(), (48, 48))
        self.player = self.player1.get_rect()
        self.player.x = self.x
        self.player.y = self.y
        
        self.bullets = []
        
    def player_movement(self):
        try:
            self.player.y += int(microy)
            self.player.x += int(microx)
            if self.player.top <= 0:
                self.player.top = 0
            if self.player.bottom >= screen_height:
                self.player.bottom = screen_height
            if self.player.right > screen_width:
                self.player.right = screen_width
            if self.player.left < 0:
                self.player.left = 0
        except:
            pass

    def player_shoot(self):
        if 'shoot' in microbitdata:
            bullet = pygame.Rect(self.player.centerx - 3, self.player.top, 7, 25)
            self.bullets.append(bullet)
        for index, item in enumerate(self.bullets):
            pygame.draw.rect(screen, 'blue', item)
        for b in range(len(self.bullets)):
            self.bullets[b][1] -= 10
        for i in self.bullets[:]:
            if i[1] < 0:
                self.bullets.remove(i)



class Enemy:
    def __init__(self):
        self.speed = 1
        self.firerate = 1
        self.x = random.randint(1, 1020)
        self.y = random.randint(10, 100)*-1
        self.enemy = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('enemy.png').convert_alpha(), (48, 48)), 180)
        self.body = self.enemy.get_rect()
        self.body.x = self.x
        self.body.y = self.y
        self.bullets = []
     
    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time % 1000 < 15:
            bullet = pygame.Rect(self.body.centerx - 3, self.body.bottom - 3, 7, 25)
            self.bullets.append(bullet)
        for index, item in enumerate(self.bullets):
            pygame.draw.rect(screen, 'crimson', item)
        for b in range(len(self.bullets)):
            self.bullets[b][1] += 10
        for i in self.bullets[:]:
            if i[1] > screen_height:
                self.bullets.remove(i)
                   
    def movement(self):
        if self.body.y < player1.player.y:
            self.body.y += self.speed
        if self.body.y > player1.player.y:
            self.body.y -= self.speed
        if self.body.x < player1.player.x:
            self.body.x += self.speed
        if self.body.x > player1.player.x:
            self.body.x -= self.speed


    
pygame.init()
clock = pygame.time.Clock()

screen_width = 1020
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space')
bg = pygame.transform.scale(pygame.image.load('space_bg.png').convert(), (screen_width, screen_height))

player1 = Player()
op1 = Enemy()
enemies = []

def spawn():
    current_time = pygame.time.get_ticks()
    if current_time % 1500 < 30:
        enemies.append(Enemy())
    for i in enemies:
        i.movement()
        i.shoot()
        screen.blit(i.enemy, i.body)

def display_score():
    global score
    game_font = pygame.font.Font('freesansbold.ttf', 30)
    s = game_font.render(f'score: {score}', False, (200, 0, 200))
    hs = game_font.render(f'high_score: {high_score}', False, (200, 0, 200))
    screen.blit(hs, (screen_width - 240, 0))
    screen.blit(s, (0, 0))
        
dead = False
score = 0
high_score = 0

explosion_anim = []
for i in range(9):
    filename = fr'C:\Users\fipha001\OneDrive - Osloskolen\py\microbit\explosions\regularExplosion0{i}.png'
    img = pygame.transform.scale(pygame.image.load(filename).convert_alpha(), (75, 75))
    img.set_colorkey('black')
    explosion_anim.append(img)
    

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = explosion_anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
                
all_sprites = pygame.sprite.Group()

while True:

    if not dead:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                th1.join()
                sys.exit()

        
        screen.blit(bg, (0, 0))
        
        for i in player1.bullets:
            for e in enemies:
                if e.body.colliderect(i):
                    enemies.remove(e)
                    score += 1
                    expl = Explosion(e.body.center)
                    all_sprites.add(expl)
                    
        for i in enemies:
            for b in i.bullets:
                if player1.player.colliderect(b):
                    expl = Explosion(player1.player.center)
                    all_sprites.add(expl)
                    dead = True
                    
        all_sprites.draw(screen)           
        all_sprites.update()

        spawn()
        player1.player_movement()
        player1.player_shoot()
        screen.blit(player1.player1, player1.player)
        display_score()
        pygame.display.flip()
        clock.tick(60)
        
    elif dead:
        if score > high_score:
            high_score = score
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                th1.join()
                sys.exit()
                
        screen.fill('black')
        display_score()
        current_time = pygame.time.get_ticks()
        game_font = pygame.font.Font('freesansbold.ttf', 70)
        if current_time % 1000 < 400:
            start = game_font.render('PRESS B TO START', False, (200, 200, 200))
            screen.blit(start, (screen_width/5 - 10, screen_height/2 + 20))
        if 'boost' in microbitdata:
            dead = False
            enemies = []
            score = 0
        pygame.display.flip()
        clock.tick(60)
            
