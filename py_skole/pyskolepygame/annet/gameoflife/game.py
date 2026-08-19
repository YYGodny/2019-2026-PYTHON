from settings import *

class Game:
    def __init__(self):
        self.surface = pygame.Surface((game_width, game_height))
        self.display_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(topleft=(padding, padding))
        self.sprites = pygame.sprite.Group()

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = (pygame.Vector2(event.pos)-(padding, padding))/cell_size
                if 0 < pos.x*cell_size < self.surface.get_width() and 0 < pos.y*cell_size < self.surface.get_height():
                    block = Block(self.sprites, (int(pos.x), int(pos.y)))
                    print(event.pos)
    
    def draw_grid(self):
        for row in range(1, rows):
            pygame.draw.line(self.surface, 'black', (0, row*cell_size), (self.surface.get_width(), row*cell_size), 1)

        for col in range(1, columns):
            pygame.draw.line(self.surface, 'black', (col*cell_size, 0), (col*cell_size, self.surface.get_height()), 1)

    def run(self):
        
        self.input()
        self.sprites.update()
        
        self.surface.fill('white')
        self.sprites.draw(self.surface)

        self.draw_grid()
        self.display_surface.blit(self.surface, self.rect)
        pygame.draw.rect(self.display_surface, 'black', self.rect, 2, 2)
        
        

class Block(pygame.sprite.Sprite):
    def __init__(self, group, pos):
        super().__init__(group)
        
        self.image = pygame.Surface((cell_size, cell_size))
        self.image.fill('blue')

        self.pos = pygame.Vector2(pos)
        self.rect = self.image.get_rect(topleft=self.pos*cell_size)
        
    def update(self):
        pass
        
        
