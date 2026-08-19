from settings import *
from game import *
from side import *

from sys import exit

class Main:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((window_width, window_height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Game Of Life')
        
        self.game = Game()
        self.side = Side()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.display_surface.fill('gray')
                    
            self.game.run()
            self.side.run()

            pygame.display.update()
            self.clock.tick()

if __name__ == '__main__':
    main = Main()
    main.run()
    
