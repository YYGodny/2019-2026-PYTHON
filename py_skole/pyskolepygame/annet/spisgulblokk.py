import pygame
import random
from sys import exit

screen_size = pygame.Vector2(900, 600)
player_size = (150, 20)

class Main:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode(screen_size)
        self.clock = pygame.time.Clock()
        self.start()

    def start(self):
        self.sprite_blocks = pygame.sprite.Group()
        self.sprite_player = pygame.sprite.Group()
        self.font = pygame.font.Font(None, 50)

        self.timers = {
            'yellowtimer': Timer(500, True, self.generate_yellow),
            'redtimer': Timer(600, True, self.generate_red),
            'increasespeed': Timer(2500, True, self.increase_speed)
            }
        
        self.timers['yellowtimer'].activate()
        self.timers['redtimer'].activate()
        self.timers['increasespeed'].activate()

        self.player = Player(self.sprite_player, player_size)

        self.speed = 2

        self.score = 0

        self.score_text = self.font.render(f'Score: {self.score}', True, 'white')

        self.game_over = Game_over()

    def generate_yellow(self):
        y = Block(self.sprite_blocks, 'yellow', (random.randint(0, int(screen_size.x)), 0), self.speed)
        
    def generate_red(self):
        r = Block(self.sprite_blocks, 'red', (random.randint(0, int(screen_size.x)), 0), self.speed)

    def increase_speed(self):
        self.speed += 1
        if self.timers['yellowtimer'].duration > 100 and self.timers['yellowtimer'].duration > 100:
            self.timers['yellowtimer'].duration -= 50
            self.timers['redtimer'].duration -= 50
    
    def timer_update(self):
        for timer in self.timers.values():
            timer.update()

    def check_collision(self):
        hits = pygame.sprite.spritecollide(self.player, self.sprite_blocks, True)
        for block in hits:
            if self.player.collide(block.farge) == True:
                self.score += 1

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_s]:
            self.player.move('right')
        if keys[pygame.K_a]:
            self.player.move('left')
                
    def check_dead(self):
        if not self.sprite_player:
            self.game_over.score = self.score
            self.game_over.run()
            self.start()
            
    def run(self):
        while True:
            self.score_text = self.font.render(f'Score: {self.score}', True, 'white')
            self.timer_update()
            self.sprite_blocks.update()
            self.sprite_player.update()
            self.input()
            self.check_dead()

            self.check_collision()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.display_surface.fill('black')

            self.sprite_blocks.draw(self.display_surface)
            self.sprite_player.draw(self.display_surface)

            self.display_surface.blit(self.score_text, (50, 50))

            pygame.display.update()
            self.clock.tick(60)

class Block(pygame.sprite.Sprite):
    def __init__(self, group, farge, pos, speed):
        super().__init__(group)
        self.farge = farge
        self.size = pygame.Vector2(30, 30)
        self.image = pygame.Surface(self.size)
        self.pos = pygame.Vector2(pos)
        
        if self.pos.x > screen_size.x-self.size.x:
            self.pos.x -= self.size.x
            
        self.rect = self.image.get_rect(topleft=self.pos)        
        self.image.fill(self.farge)

        self.gravity = speed

    def move(self):
        self.rect.y += self.gravity
        if self.rect.y > screen_size.y:
            self.kill()
            
    def update(self):
        self.move()
        

class Player(pygame.sprite.Sprite):
    def __init__(self, group, size):
        super().__init__(group)
        self.size = size
        self.pos = pygame.Vector2(int(screen_size.x/2), screen_size.y)
        self.image = pygame.Surface(self.size)
        self.rect = self.image.get_rect(midbottom = self.pos)
        self.image.fill('gray')

        self.movementspeed = 4

    def collide(self, farge):
        if farge == 'yellow':
            return True
        if farge == 'red':
            self.kill()

    def move(self, direction):
        if self.rect.right + self.movementspeed < screen_size.x:
            if direction == 'right':
                self.rect.x += self.movementspeed
        if self.rect.left - self.movementspeed > 0:
            if direction == 'left':
                self.rect.x -= self.movementspeed       

class Timer:
    def __init__(self, duration, repeated=False, func=None):
        self.repeated = repeated
        self.func = func
        self.duration = duration

        self.start_time = 0
        self.active = False
        
    def activate(self):
        self.active = True
        self.start_time = pygame.time.get_ticks()

    def deactivate(self):
        self.active = False
        self.start_time = 0
        
    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.start_time >= self.duration and self.active:

            if self.func and self.start_time != 0:
                self.func()

            self.deactivate()

            if self.repeated:
                self.activate()

class Game_over:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(None, 50)
        self.clock = pygame.time.Clock()
        
        self.text = self.font.render('Game Over!', True, 'white')
        self.text_rect = self.text.get_rect(center=(screen_size.x/2, screen_size.y/2))

        self.score = 0

        self.score_text = self.font.render(f'Du fikk: {self.score}!', True, 'white')
        self.score_text_rect = self.text.get_rect(center=(screen_size.x/2, screen_size.y/2 + 100))

        self.start_button = pygame.Rect(screen_size.x/2 - 70, screen_size.y/2 + 200, 100, 70)
        self.start_text = self.font.render(f'Start', True, 'black')
        self.click = False
        self.running = True

    def input(self, events):
        self.mx, self.my = pygame.mouse.get_pos()
        self.click = False
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True

    def buttonpress(self):
        if self.start_button.collidepoint((self.mx, self.my)):
            if self.click:
                self.running = False

    def render(self):
        pygame.draw.rect(self.display_surface, (255, 0, 0), self.start_button)
        self.score_text = self.font.render(f'Du fikk: {self.score}!', True, 'white')
        self.display_surface.blit(self.text, self.text_rect)
        self.display_surface.blit(self.score_text, self.score_text_rect)
        self.display_surface.blit(self.start_text, (self.start_button.x + 10, self.start_button.y + 15))

    def run(self):
        while self.running:
            events = pygame.event.get()
            self.input(events)
            self.buttonpress()
            self.display_surface.fill('black')
            self.render()
            
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
            pygame.display.update()
            self.clock.tick(60)

main = Main()
main.run()
