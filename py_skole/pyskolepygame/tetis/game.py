from settings import *
from random import choice
from sys import exit
from os.path import join

from timer import Timer

class Game:
    def __init__(self, get_next_shape, update_score):

        #general
        self.surface = pygame.Surface((game_width, game_height))
        self.display_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(topleft = (padding, padding))
        self.sprites = pygame.sprite.Group()

        #game connection
        self.get_next_shape = get_next_shape
        self.update_score = update_score
        
        #lines
        self.line_surface = self.surface.copy()
        self.line_surface.fill((0, 255, 0))
        self.line_surface.set_colorkey((0, 255, 0))
        self.line_surface.set_alpha(120)

        #tetromino
        self.field_data = [[0 for i in range(columns)] for y in range(rows)]
        self.tetromino = Tetromino(
            choice(list(TETROMINOS.keys())),
            self.sprites,
            self.create_new_tetromino,
            self.field_data
            )

        #timer
        self.down_speed = update_start_speed
        self.down_speed_faster = self.down_speed * 0.3
        self.down_pressed = False
        self.timers = {
            'vertical move': Timer(self.down_speed, True, self.move_down),
            'horizontal move': Timer(move_wait_time),
            'rotate': Timer(rotate_wait_time)
            }
        self.timers['vertical move'].activate()

        #score
        self.current_level = 1
        self.current_score = 0
        self.current_lines = 0

        #sound
        self.landing_sound = pygame.mixer.Sound(join('sound', 'landing.wav'))
        self.landing_sound.set_volume(0.1)

    def calculate_score(self, num_lines):
        self.current_lines += num_lines
        self.current_score += score_data[num_lines] * self.current_level

        if self.current_lines / 10 > self.current_level:
            self.current_level += 1
            self.down_speed *= 0.75
            self.down_speed_faster = self.down_speed * 0.3
            self.timers['vertical move'].duration = self.down_speed
            
        self.update_score(self.current_lines, self.current_score, self.current_level) 

    def check_game_over(self):
        for block in self.tetromino.blocks:
            if block.pos.y < 0:
                pygame.quit()
                exit()
            
    def create_new_tetromino(self):
        self.landing_sound.play()
        self.check_game_over()
        self.check_finished_rows()
        self.tetromino = Tetromino(
            self.get_next_shape(),
            self.sprites,
            self.create_new_tetromino,
            self.field_data
            )
        
    def timer_update(self):
        for timer in self.timers.values():
            timer.update()
            
    def move_down(self):
        self.tetromino.move_down()
    
    def draw_grid(self):
        
        for col in range(1, columns):
            pygame.draw.line(self.line_surface, line_color, (col*cell_size, 0), (col*cell_size, self.surface.get_height()), 1)

        for row in range(1, rows):
            pygame.draw.line(self.line_surface, line_color, (0, row*cell_size), (self.surface.get_width(), row*cell_size), 1)

        self.surface.blit(self.line_surface, (0,0))

    def input(self):
        keys = pygame.key.get_pressed()

        #checking horizontal movement
        if not self.timers['horizontal move'].active:
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.tetromino.move_horizontal(-1)
                self.timers['horizontal move'].activate()
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.tetromino.move_horizontal(1)
                self.timers['horizontal move'].activate()

        #check for rotation
        if not self.timers['rotate'].active:
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.tetromino.rotate()
                self.timers['rotate'].activate()

        #down speedup
        if not self.down_pressed and (keys[pygame.K_DOWN] or keys[pygame.K_s]):
            self.down_pressed = True
            self.timers['vertical move'].duration = self.down_speed_faster

        if self.down_pressed and not (keys[pygame.K_DOWN] or keys[pygame.K_s]):
            self.down_pressed = False
            self.timers['vertical move'].duration = self.down_speed
        
        
    def check_finished_rows(self):

        #get the full row indexes
        delete_rows = []
        for i, row in enumerate(self.field_data):
            if all(row):
                delete_rows.append(i)

        if delete_rows:
            for delete_row in delete_rows:

                #delete full rows
                for block in self.field_data[delete_row]:
                    block.kill()

                #move down the blocks
                for row in self.field_data:
                    for block in row:
                        if block and block.pos.y < delete_row:
                            block.pos.y += 1
                            

            #rebuild the field data
            self.field_data = [[0 for i in range(columns)] for y in range(rows)]
            for block in self.sprites:
                self.field_data[int(block.pos.y)][int(block.pos.x)] = block
                
            #update score
            self.calculate_score(len(delete_rows))
         
    def run(self):

        #update
        self.input()
        self.timer_update()
        self.sprites.update()

        #drawing
        self.surface.fill(gray)
        self.sprites.draw(self.surface)

        self.draw_grid()
        self.display_surface.blit(self.surface, (padding, padding))
        pygame.draw.rect(self.display_surface, line_color, self.rect, 2, 2)

class Tetromino:
    def __init__(self, shape, group, create_new_tetromino, field_data):

        #setup
        self.shape = shape
        self.block_positions = TETROMINOS[shape]['shape']
        self.color = TETROMINOS[shape]['color']
        self.create_new_tetromino = create_new_tetromino
        self.field_data = field_data

        #create blocks
        self.blocks = [Block(group, pos, self.color) for pos in self.block_positions]

    #collisions
    def next_move_horisontal_collide(self, blocks, amount):
        collision_list = [block.horizontal_collide(int(block.pos.x + amount), self.field_data) for block in self.blocks]
        return True if any(collision_list) else False

    def next_move_vertical_collide(self, blocks, amount):
        collision_list = [block.vertical_collide(int(block.pos.y + amount), self.field_data) for block in self.blocks]
        return True if any(collision_list) else False

    #movements
    def move_horizontal(self, amount):
        if not self.next_move_horisontal_collide(self.blocks, amount):
            for block in self.blocks:
                block.pos.x += amount
        
    def move_down(self):
        if not self.next_move_vertical_collide(self.blocks, 1):
            for block in self.blocks:
                block.pos.y += 1
        else:
            for block in self.blocks:
                self.field_data[int(block.pos.y)][int(block.pos.x)] = block
            self.create_new_tetromino()
            
    #rotate
    def rotate(self):
        if self.shape != 'O':

            #1. pivot point
            pivot_pos = self.blocks[0].pos

            #2. new block positions
            new_block_positions = [block.rotate(pivot_pos) for block in self.blocks]

            #3. collision check
            for pos in new_block_positions:
                #horizontal
                if pos.x < 0 or pos.x >= columns:
                    return

                #field check -> collision with other pieces
                if self.field_data[int(pos.y)][int(pos.x)]:
                    return

                #vertical / floor check
                if pos.y > rows:
                    return
            
            #4. implement new positions
            for i, block in enumerate(self.blocks):
                block.pos = new_block_positions[i]
                
class Block(pygame.sprite.Sprite):
    def __init__(self, group, pos, color):
        super().__init__(group)

        #general
        self.image = pygame.Surface((cell_size, cell_size))
        self.image.fill(color)

        #position
        self.pos = pygame.Vector2(pos) + block_offset
        self.rect = self.image.get_rect(topleft=self.pos*cell_size)

    def rotate(self, pivot_pos):
        return pivot_pos + (self.pos - pivot_pos).rotate(90)

    def horizontal_collide(self, x, field_data):
        if not 0 <= x < columns:
            return True
        if field_data[int(self.pos.y)][x]:
            return True

    def vertical_collide(self, y, field_data):
        if y >= rows:
            return True
        if y >= 0 and field_data[y][int(self.pos.x)]:
            return True
        
    def update(self):
        self.rect.topleft = self.pos*cell_size

    
        
        
