from settings import *

#fikser på hvordan det ser ut senere, men dette får gå

class Menu:
    def __init__(self):
        pygame.mouse.set_visible(True)
        self.display_surface = pygame.display.get_surface()
        self.display_surface.fill((255, 255, 255))

        self.button_start = pygame.Rect(100, 200, 200, 50)    

        #player1
        self.blue_button = pygame.Rect(425, 350, 100, 50)
        self.green_button = pygame.Rect(525, 350, 100, 50)
        self.red_button = pygame.Rect(625, 350, 100, 50)

        #player2
        self.blue_button2 = pygame.Rect(775, 350, 100, 50)
        self.green_button2 = pygame.Rect(875, 350, 100, 50)
        self.red_button2 = pygame.Rect(975, 350, 100, 50) 
                

        self.click = False
        self.running = True

        self.player1 = 'green'
        self.player2 = 'green'

    def input(self, events):
        self.mx, self.my = pygame.mouse.get_pos()
        self.click = False
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True

    def draw_text(self, text, size, color, surface, x, y):
        self.font = pygame.font.SysFont(None, size)
        textobj = self.font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def button_press(self):
        if self.button_start.collidepoint((self.mx, self.my)):
            if self.click:
                self.running = False
        if self.blue_button.collidepoint((self.mx, self.my)):
            if self.click:
                self.player1 = 'blue'
        if self.red_button.collidepoint((self.mx, self.my)):
            if self.click:
                self.player1 = 'red'
        if self.green_button.collidepoint((self.mx, self.my)):
            if self.click:
                self.player1 = 'green'

        if self.blue_button2.collidepoint((self.mx, self.my)):
            if self.click:
                self.player2 = 'blue'
        if self.red_button2.collidepoint((self.mx, self.my)):
            if self.click:
                self.player2 = 'red'
        if self.green_button2.collidepoint((self.mx, self.my)):
            if self.click:
                self.player2 = 'green'

    def render(self):
        pygame.draw.rect(self.display_surface, (255, 0, 0), self.button_start)
        self.draw_text('Main Menu', 75, 'black', self.display_surface, 100, 100)
        self.draw_text('Start', 35, 'white', self.display_surface, 150, 215)
        self.draw_text('Press Esc to exit', 50, 'black', self.display_surface, 800, 50)

        self.draw_text('Player1: WASD, FGH, Space', 30, 'black', self.display_surface, 500, 600)
        self.draw_text('Player2: ARROWKEYS, komma punktum bindestrek, rightshift', 30, 'black', self.display_surface, 500, 650)

        #select seksjonen
        self.draw_text('Player 1', 50, 'black', self.display_surface, 500, 200)
        self.draw_text('Player 2', 50, 'black', self.display_surface, 850, 200)

        pygame.draw.rect(self.display_surface, (0, 0, 255), self.blue_button)
        pygame.draw.rect(self.display_surface, (0, 255, 0), self.green_button)
        pygame.draw.rect(self.display_surface, (255, 0, 0), self.red_button)

        pygame.draw.rect(self.display_surface, (0, 0, 255), self.blue_button2)
        pygame.draw.rect(self.display_surface, (0, 255, 0), self.green_button2)
        pygame.draw.rect(self.display_surface, (255, 0, 0), self.red_button2)

        self.draw_text(f'Player 1 selected: {self.player1}', 25, 'black', self.display_surface, 425, 500)
        self.draw_text(f'Player 2 selected: {self.player2}', 25, 'black', self.display_surface, 775, 500)
    
    def run(self, events):
        self.input(events)
        self.button_press()
        self.render()
        
