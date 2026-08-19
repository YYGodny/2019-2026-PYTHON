import serial
import time
import pygame
import sys
import threading
import random

#serial
ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM5'
ser.open()


def microbit_input():
    global microbitdata
    while True:
        microbitdata = str(ser.readline())
        microbitdata = microbitdata.split("'")[1]
        microbitdata = microbitdata.replace(' ', '')
        microbitdata = microbitdata.replace('\\r', '')
        microbitdata = microbitdata.replace('\\n', '')

        
th1 = threading.Thread(target=microbit_input, daemon = True)
th1.start()

#pygame
pygame.init()
clock = pygame.time.Clock()

screen_width = 1020
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

ball = pygame.Rect(screen_width/2- 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)
current_pl_cl = 0
colours = ['blue', 'aliceblue', 'aqua', 'brown', 'blueviolet', 'burlywood',
           'cadetblue1', 'chartreuse', 'chocolate', 'crimson',
            'cornflowerblue', 'cyan', 'darkgoldenrod', 'deeppink',
           'darkviolet'
            ]

ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
opponent_speed = 15

paused_font = pygame.font.Font('freesansbold.ttf', 70)
player_score = 0
opponent_score = 0
game_font = pygame.font.Font('freesansbold.ttf', 32)

score_time = True

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
        
    if ball.left <= 0:
        player_score += 1
        score_time = pygame.time.get_ticks()
        
    if ball.right >= screen_width:
        opponent_score += 1
        score_time = pygame.time.get_ticks()
        
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    try:
        if int(microbitdata) > 150 or int(microbitdata) < -150:
            pass
        player.y += int(microbitdata)
        if player.top <= 0:
            player.top = 0
        if player.bottom >= screen_height:
            player.bottom = screen_height
    except:
        pass

def opponent_animation():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height 

def ball_start():
    global ball_speed_x, ball_speed_y, score_time

    current_time = pygame.time.get_ticks()
    ball.center = (screen_width/2, screen_height/2)

    if current_time - score_time < 700:
        number_three = game_font.render('3', False, light_grey)
        screen.blit(number_three, (screen_width/2 - 10, screen_height/2 + 20))
    if 700 < current_time - score_time < 1400:
        number_two = game_font.render('2', False, light_grey)
        screen.blit(number_two, (screen_width/2 - 10, screen_height/2 + 20))
    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render('1', False, light_grey)
        screen.blit(number_one, (screen_width/2 - 10, screen_height/2 + 20))
        
    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0, 0
    else:
        ball_speed_y = 7 * random.choice((1,-1))
        ball_speed_x = 7* random.choice((1,-1))
        score_time = None

def pause_game():
    global paused, gaming
    if microbitdata == '!':
        if paused == False and gaming == True:
            paused = True
            gaming = False
        else:
            gaming = True
            paused = False
        
paused = False
gaming = True

while True:
        
    if gaming:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                th1.join()
                sys.exit()

        if '?' in microbitdata:
            current_pl_cl = random.randint(0, len(colours) - 1)
            
        ball_animation()
        player_animation()
        opponent_animation()      
        pause_game()
        
        screen.fill(bg_color)
        pygame.draw.rect(screen, colours[current_pl_cl], player) 
        pygame.draw.rect(screen, light_grey, opponent)
        pygame.draw.ellipse(screen, light_grey, ball)
        pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2, screen_height))

        if score_time:
            ball_start()
        
        player_text = game_font.render(f'{player_score}', False, light_grey)
        screen.blit(player_text, (550, 350))

        opponent_text = game_font.render(f'{opponent_score}', False, light_grey)
        screen.blit(opponent_text, (450, 350))
        
        pygame.display.flip()
        clock.tick(60)
        
    elif paused:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                th1.join()
                sys.exit()
                
        paused_text = paused_font.render('PAUSED', False, light_grey)
        screen.blit(paused_text, (370, 350))
        pause_game()

        pygame.display.flip()
        clock.tick(60)
