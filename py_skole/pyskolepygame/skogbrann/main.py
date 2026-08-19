from settings import *
from game import *

class Main:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((window_width, window_height))
        self.clock = pygame.time.Clock()
        self.game = Game()
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.display_surface.fill('white')

            self.game.run()

            pygame.display.update()
            self.clock.tick()

main = Main()
main.run()
