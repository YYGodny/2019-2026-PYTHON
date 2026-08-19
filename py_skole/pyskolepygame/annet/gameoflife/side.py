from settings import *

class Side:
    def __init__(self):
        self.surface = pygame.Surface((side_width, side_height))
        self.display_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(topleft=(padding*2+game_width, padding))       
        self.sprites = pygame.sprite.Group()
        self.button_start = Button(self.sprites, (padding, padding), 'Start')
        self.button_reset = Button(self.sprites, (padding, padding), 'Reset')
        
    def run(self):
        self.surface.fill('white')

        self.sprites.draw(self.surface)
        
        self.display_surface.blit(self.surface, self.rect)


class Button(pygame.sprite.Sprite):
    def __init__(self, group, pos, text):
        super().__init__(group)
        self.image = pygame.Surface((button_width, button_height))
        self.rect = self.image.get_rect(topleft = pos)
        self.image.fill('yellow')

        font = pygame.font.SysFont('Arial', 40)
        self.text_surface = font.render(text, True, 'black')

    def update(self):
        self.image.blit(self.text_surface, self.rect)
