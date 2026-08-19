from settings import *
from pygame.image import load
from pygame.transform import scale_by
from os import path

class Preview:
    def __init__(self):

        #general
        self.surface = pygame.Surface((sidebar_width, game_height*preview_height_fraction))
        self.rect = self.surface.get_rect(topright = (window_width-padding, padding))
        self.display_surface = pygame.display.get_surface()

        #shapes
        self.shape_surfaces = {shape: scale_by(load(path.join('graphics', f'{shape}.png')).convert_alpha(), 0.75) for shape in TETROMINOS.keys()}

        #image position data
        self.increment_height = self.surface.get_height() / 3
        
    def display_pieces(self, shapes):
        for i, shape in enumerate(shapes):
            shape_surface = self.shape_surfaces[shape]
            x = self.surface.get_width() / 2
            y = self.increment_height / 2 + i * self.increment_height
            rect = shape_surface.get_rect(center = (x, y))
            self.surface.blit(shape_surface, rect)
            
    def run(self, next_shapes):
        self.surface.fill(gray)
        self.display_pieces(next_shapes)
        self.display_surface.blit(self.surface, self.rect)
        pygame.draw.rect(self.display_surface, line_color, self.rect, 2, 2)
