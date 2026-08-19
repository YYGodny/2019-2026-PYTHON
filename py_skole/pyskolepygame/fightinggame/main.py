from settings import *
from game import *
from sys import exit
from menu import *

class Main:
    def __init__(self):
        #general
        pygame.init()
        self.display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Racoon')

        self.game = Game('green', 'green')
        self.menu = Menu()

        self.state = 'menu'
    
    def run(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
            #display
            self.display_surface.fill('white')
            
            #game components
            if self.state == 'menu':
                self.menu.run(events)
            
            if self.menu.running == False:
                if self.state == 'menu':
                    self.game = Game(self.menu.player1, self.menu.player2)
                    self.state = 'game'
                    
            if self.state == 'game':
                self.game.run(events)

            if self.game.running == False:
                if self.state == 'game':
                    self.menu = Menu()
                    self.state = 'menu'
            
            #update game
            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    main = Main()
    main.run()
            
                    
        
    
