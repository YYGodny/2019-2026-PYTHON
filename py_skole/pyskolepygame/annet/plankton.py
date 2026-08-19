import pygame
import random
from sys import exit

screen_size = pygame.Vector2(700, 500)
bunndyr_start_size = (100, 50)

class Main:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode(screen_size)
        self.clock = pygame.time.Clock()
        self.sprite_plankton = pygame.sprite.Group()
        self.sprite_bunndyr = pygame.sprite.Group()
        self.font = pygame.font.Font(None, 50)

        self.timers = {
            'planktontimer': Timer(500, True, self.generate_plankton),
            'redplanktontimer': Timer(700, True, self.generate_rødplankton)
            }
        self.timers['planktontimer'].activate()
        self.timers['redplanktontimer'].activate()

        self.bunndyr = bunndyr(self.sprite_bunndyr, bunndyr_start_size)

        self.time_text = self.font.render(f'{self.timers["planktontimer"].duration/1000}sekund pr plankton', True, 'white')

    def generate_plankton(self):
        p = plankton(self.sprite_plankton, 'green', (random.randint(0, int(screen_size.x)), 0))
        
    def generate_rødplankton(self):
        p = plankton(self.sprite_plankton, 'red', (random.randint(0, int(screen_size.x)), 0))
    
    def timer_update(self):
        for timer in self.timers.values():
            timer.update()

    def check_collision(self):
        hits = pygame.sprite.spritecollide(self.bunndyr, self.sprite_plankton, True)
        for plankton in hits:
            self.bunndyr.endre(plankton.farge)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.timers['planktontimer'].duration += 10
        if keys[pygame.K_DOWN]:
            if self.timers['planktontimer'].duration - 10 > 0:
                self.timers['planktontimer'].duration -= 10
                
    def check_dead(self):
        if not self.sprite_bunndyr:
            pygame.quit()
            
    def run(self):
        while True:
            self.time_text = self.font.render(f'{self.timers["planktontimer"].duration/1000}sekund pr plankton', True, 'white')
            self.timer_update()
            self.sprite_plankton.update()
            self.sprite_bunndyr.update()
            self.input()
            self.check_dead()

            self.check_collision()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.display_surface.fill('black')

            self.sprite_plankton.draw(self.display_surface)
            self.sprite_bunndyr.draw(self.display_surface)

            self.display_surface.blit(self.time_text, (50, 50))

            pygame.display.update()
            self.clock.tick(60)

class plankton(pygame.sprite.Sprite):
    def __init__(self, group, farge, pos):
        super().__init__(group)
        self.farge = farge
        self.size = pygame.Vector2(30, 30)
        self.image = pygame.Surface(self.size)
        self.pos = pygame.Vector2(pos)
        if self.pos.x > screen_size.x-self.size.x:
            self.pos.x -= self.size.x
        self.font = pygame.font.Font(None, 50)
        self.rect = self.image.get_rect(topleft=self.pos)
        if self.farge == 'green':
            fontobj = self.font.render('G', True, 'black')
        elif self.farge == 'red':
            fontobj = self.font.render('R', True, 'black')
        self.image.fill(self.farge)
        self.image.blit(fontobj, (0,0))

        self.gravity = 2

    def move(self):
        self.rect.y += self.gravity
        if self.rect.y > screen_size.y:
            self.kill()
            
    def update(self):
        self.move()
        

class bunndyr(pygame.sprite.Sprite):
    def __init__(self, group, startsize):
        super().__init__(group)
        self.startsize = pygame.Vector2(startsize)
        self.pos = pygame.Vector2(int(screen_size.x/2), screen_size.y)
        self.size = pygame.Vector2(self.startsize)
        self.image = pygame.Surface(self.size)
        self.rect = self.image.get_rect(midbottom = self.pos)
        self.image.fill('gray')

    def endre(self, farge):
        if farge == 'green':
            self.size.x += 20
        if farge == 'red':
            self.size.x -= 20

    def check_status(self):
        if self.size.x < self.startsize.x:
            self.kill()
        if self.size.x >= screen_size.x:
            self.kill()

    def update(self):
        self.check_status()
        self.image = pygame.Surface(self.size)
        self.image.fill('gray')
        self.rect = self.image.get_rect(midbottom = self.pos)
        

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



main = Main()
main.run()
