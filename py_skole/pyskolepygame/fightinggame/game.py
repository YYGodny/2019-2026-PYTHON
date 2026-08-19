from settings import *
from timer import *
from os.path import join
from os import listdir
from pygame.transform import scale_by
from pygame.image import load

class Game:
    def __init__(self, p1, p2):
        self.display_surface = pygame.display.get_surface()
        self.surface = pygame.Surface((map_width, map_height))
        self.screen_width, self.screen_height = self.display_surface.get_size()
        self.sprite_characters = pygame.sprite.Group()
        self.sprite_attacks1 = pygame.sprite.Group()
        self.sprite_attacks2 = pygame.sprite.Group()
        self.sprite_healthbar = pygame.sprite.Group()

        self.running = True
        pygame.mouse.set_visible(False)
        
##        #slett
##        self.mouse_group = pygame.sprite.Group()

        #images
        self.platform_image = load(join('assets', 'map1.png')).convert_alpha()
        self.platform_image_rect = self.platform_image.get_rect(center=(self.screen_width/2, self.screen_height/2))
        
        self.bg = load(join('assets', 'ocean_cloud_bg', 'Ocean_5', '5.png')).convert_alpha()
        self.bg = pygame.transform.scale(self.bg, (self.screen_width, self.screen_height))

        #objects
        self.platform = Platform()
        self.platform.create_rects(pygame.Vector2(self.platform_image_rect.topleft))

        self.characters = {
            'blue': Blue,
            'red': Red,
            'green': Green,
            }

        self.player1 = self.characters[p1](self.sprite_characters, self.sprite_attacks1)
        self.player2 = self.characters[p2](self.sprite_characters, self.sprite_attacks2, True)

        self.healthbar1 = Healthbar(self.sprite_healthbar, self.player1.health, healthpos1)
        self.healthbar2 = Healthbar(self.sprite_healthbar, self.player2.health, healthpos2)

        #timers
        self.timers = {
            }
    
    def draw_grid(self):
        for row in range(1, rows):
            pygame.draw.line(self.display_surface, 'white', (self.platform_image_rect.left, self.platform_image_rect.top+row*cell_size), (self.platform_image_rect.right, self.platform_image_rect.top+row*cell_size), 2)

        for col in range(1, columns):
            pygame.draw.line(self.display_surface, 'white', (self.platform_image_rect.left+col*cell_size, self.platform_image_rect.top), (self.platform_image_rect.left+col*cell_size, self.platform_image_rect.bottom), 2)

    def timer_update(self):
        for timer in self.timers.values():
            timer.update()
    
    def input(self, events):
        keys = pygame.key.get_pressed()
        
        self.player1.x_direction = None
        self.player1.y_direction = None
        self.player2.x_direction = None
        self.player2.y_direction = None
        
        if keys[pygame.K_a]:
            self.player1.x_direction = 'left'
        if keys[pygame.K_d]:
            self.player1.x_direction = 'right'
        if keys[pygame.K_w]:
            self.player1.y_direction = 'up'
        if keys[pygame.K_s]:
            self.player1.y_direction = 'down'

        if keys[pygame.K_LEFT]:
            self.player2.x_direction = 'left'
        if keys[pygame.K_RIGHT]:
            self.player2.x_direction = 'right'
        if keys[pygame.K_UP]:
            self.player2.y_direction = 'up'
        if keys[pygame.K_DOWN]:
            self.player2.y_direction = 'down'
        
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player1.jump()
                if event.key == pygame.K_h:
                    self.player1.dodge()
                if event.key == pygame.K_f:
                    self.player1.light_attack()
                if event.key == pygame.K_g:
                    self.player1.heavy_attack()

                if event.key == pygame.K_RSHIFT:
                    self.player2.jump()
                if event.key == pygame.K_COMMA:
                    self.player2.dodge()
                if event.key == pygame.K_MINUS:
                    self.player2.light_attack()
                if event.key == pygame.K_PERIOD:
                    self.player2.heavy_attack()

        
        self.player1.move(self.platform.rects)
        self.player2.move(self.platform.rects)

##        ### slett #########################
##        pygame.mouse.set_visible(False)
##        self.pos = pygame.mouse.get_pos()
##        self.a = pygame.Surface((10, 10))
##        self.a.fill('red')
##        self.am = pygame.mask.from_surface(self.a)
        
    def collisions(self):
        hits = pygame.sprite.spritecollide(self.player1, self.sprite_attacks2, False, pygame.sprite.collide_mask)
        
        for attack in hits:
            self.player1.get_hit(attack)
            
        hits = pygame.sprite.spritecollide(self.player2, self.sprite_attacks1, False, pygame.sprite.collide_mask)
        
        for attack in hits:
            self.player2.get_hit(attack)

        self.healthbar1.change(self.player1.damagetaken)
        self.healthbar2.change(self.player2.damagetaken)
        
    def check_dead(self):
        if self.player1.dead or self.player2.dead:
            self.running = False
            

            
    def run(self, events):
        #update
        self.input(events)
        self.timer_update()
        self.sprite_characters.update()
        self.sprite_attacks1.update()
        self.sprite_attacks2.update()
        self.sprite_healthbar.update()
        
        self.collisions()
        self.check_dead()
        
        #images
        self.display_surface.blit(self.bg, (0, 0))
        self.display_surface.blit(self.platform_image, self.platform_image_rect)
        
##        #sleett"""""""""""####################
##        if self.player1.mask.overlap(self.am, (self.pos[0]-self.player1.rect.x, self.pos[1] -self.player1.rect.y)):
##            col = 'red'
##        else:
##            col = 'green'
##        self.a.fill(col)
##        self.display_surface.blit(self.a, self.pos)
        
        
        #components
        self.sprite_characters.draw(self.display_surface)
        self.sprite_attacks1.draw(self.display_surface)
        self.sprite_attacks2.draw(self.display_surface)
        self.sprite_healthbar.draw(self.display_surface)
##        pygame.draw.rect(self.display_surface, 'black', self.player1.rect, 2)
##        pygame.draw.rect(self.display_surface, 'red', self.player1.hitbox, 2)
##        pygame.draw.rect(self.display_surface, 'black', self.player2.rect, 2)
##        pygame.draw.rect(self.display_surface, 'red', self.player2.hitbox, 2)
##        self.display_surface.blit(self.player1.mask.to_surface(), (0, 0))
        
class Platform:
    def __init__(self):
        self.rects = []

    def create_rects(self, image_topleft):
        for y, row in enumerate(TILE_DATA):
            for x, tile in enumerate(row):
                if tile in (65, 128, 19, 130, 67):
                    tile_rect = pygame.Rect(image_topleft[0] + x*cell_size, image_topleft[1] + y*cell_size + offset, cell_size, cell_size-offset)
                    self.rects.append(tile_rect)
                elif tile >= 0:
                    tile_rect = pygame.Rect(image_topleft[0] + x*cell_size, image_topleft[1] + y*cell_size, cell_size, cell_size)
                    self.rects.append(tile_rect)
                    
    def draw_rects(self, surface):
        [pygame.draw.rect(surface, 'black', i) for i in self.rects]

class Characters(pygame.sprite.Sprite):
    def __init__(self, group, attackgroup, spawnopposite=False):
        super().__init__(group)
        self.spawn = pygame.Vector2((13, 4))
        if spawnopposite:
            self.spawn = pygame.Vector2((26, 4))
        self.image = pygame.Surface((32, 32))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=self.spawn*cell_size)
        self.mask = pygame.mask.from_surface(self.image)
        self.flip = False

        self.health = None
        self.damagetaken = 0
        self.percentageboost = 0
        self.dead = False

        self.vel_y = 0
        self.vel_x = 0
        self.inair = True
        self.jump_count = 0
        self.x_direction = None
        self.y_direction = None

        #animation
        self.frame = 0
        self.anim_steps = 6

        self.sprite_attacks = attackgroup
        self.light_anim = {
            'side': [scale_by(load(join('assets', 'lightattacks', 'side', 'FE1002', i)).convert_alpha(), 3) for i in listdir(join('assets', 'lightattacks', 'side', 'FE1002'))],
            'up': [scale_by(load(join('assets', 'lightattacks', 'up', 'SFX303_nyknck', i)).convert_alpha(), 2.5) for i in listdir(join('assets', 'lightattacks', 'up', 'SFX303_nyknck'))],
            'down': [scale_by(load(join('assets', 'lightattacks', 'down', 'SP602_nyknck', i)).convert_alpha(), 2.5) for i in listdir(join('assets', 'lightattacks', 'down', 'SP602_nyknck'))]
            }
        
        #timer
        self.timers = {
            'light' : Timer(LIGHT),
            'light_cooldown' : Timer(light_cooldown),
            'heavy' : Timer(HEAVY),
            'special_anim_dur': Timer(HEAVY),
            'heavy_cooldown' : Timer(heavy_cooldown),
            'animation': Timer(animation_time, True, self.update_animation),
            'dodge_cooldown': Timer(dodge_cooldown),
            'dodge_duration': Timer(dodge_duration),
            'hit_duration': Timer(hit_duration),
            }

        self.timers['animation'].activate()

    def get_image(self, frame, sheet, width, height, scale=2, color='black', row=0):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(sheet, (0, 0), (frame*width, row*height, width, height))
        image = pygame.transform.scale(image, (width*scale, height*scale))
        image.set_colorkey(color)
        return image

    def get_max_rect(self, anim_list):
        hitbox = None
        for anim in anim_list.values():
            for frame in anim:
                rect = frame.get_bounding_rect()
                if hitbox is None:
                    hitbox = rect.copy()
                else:
                    #fra chatgpt, basically lager en rect som har en minimum størrelse som inneholder begge rektanglene. Man kombinerer rektanglene, også med tanke på position.
                    hitbox.union_ip(rect)

        return hitbox

    def crop_image(self, image, rect):
        return image.subsurface(rect).copy()

    def update_animation(self):
        self.frame += 1
        if self.frame == self.anim_steps and self.anim == self.anim_list['falling']:
            self.frame = self.anim_steps - 1
        elif self.frame >= self.anim_steps:
            self.frame = 0
            

    def change_animation(self, animation):
        if self.anim != self.anim_list[animation]:
            self.anim = self.anim_list[animation]
            self.anim_steps = len(self.anim)
            self.frame = 0
    
    def timer_update(self):
        for timer in self.timers.values():
            timer.update()

    def get_hit(self, attack):
        if self.timers['dodge_duration'].active or self.timers['hit_duration'].active:
            return
        self.timers['hit_duration'].activate()
        self.damagetaken += attack.damage
        self.percentageboost = (self.damagetaken/self.health)*10
        
        if self.hitbox.left <= attack.prect.left:
            self.vel_x -= attack.knockback.x * (1+self.percentageboost)
        if self.hitbox.right > attack.prect.right:
            self.vel_x += attack.knockback.x * (1+self.percentageboost)
        self.vel_y += attack.knockback.y * (1+self.percentageboost/5)

    def light_attack(self):
        if not self.timers['light_cooldown'].active and not self.timers['heavy_cooldown'].active:
            adir = None
            if self.x_direction:
                adir = 'side'
            elif self.y_direction:
                adir = self.y_direction
            else:
                adir = 'up'
            current_attack = (self.light_anim[adir], self.x_direction == 'left')
                
            self.timers['light'].activate()
            self.timers['light_cooldown'].activate()
            attack = Attacks(self.sprite_attacks, current_attack, LIGHT, self.hitbox, adir, light_damage[adir], light_knockback[adir])

    def heavy_attack(self):
        if not self.timers['heavy_cooldown'].active and not self.timers['light_cooldown'].active and not self.timers['hit_duration'].active:
            adir = None
            if self.x_direction:
                adir = 'side'
            elif self.y_direction:
                adir = self.y_direction
            else:
                adir = 'up'
            current_attack = (self.heavy_anim[adir], self.x_direction == 'left')
                
            self.timers['heavy'].activate()
            self.timers['heavy_cooldown'].activate()
            if adir == 'up':
                self.timers['special_anim_dur'].activate()
             
            attack = Attacks(self.sprite_attacks, current_attack, HEAVY, self.hitbox, adir, heavy_damage[adir], heavy_knockback[adir], adir == 'up', True)

    def dodge(self):
        if not self.timers['dodge_cooldown'].active:
            self.timers['dodge_cooldown'].activate()
            self.timers['dodge_duration'].activate()
            
    def jump(self):
        if not self.timers['heavy'].active:
            if self.jump_count < 4:
                self.jump_count += 1
                self.vel_y = jump
                self.inair = True
                self.change_animation('idle')
                self.change_animation('jump')
           
    def move(self, tile_rects):
        dx = 0
        dy = 0
        
        #lager en rect under self.rect for å sjekke om det er bakke under recten
        if pygame.Rect(self.hitbox.left, self.hitbox.bottom, self.hitbox.width, 2).collidelist(tile_rects) == -1:
            self.inair = True
        
        if self.x_direction == None and self.y_direction == None and self.vel_y == 0 and self.vel_x == 0:
            if self.anim == self.anim_list['landing'] and self.frame < self.anim_steps-1:
                pass
            else:
                self.change_animation('idle')
           
        if self.inair and self.vel_y > 1:
            self.change_animation('falling')

        if not self.timers['light'].active or self.inair:     
            if self.x_direction == 'right':
                self.vel_x += movement
                if not self.inair and not self.timers['light'].active and not self.timers['heavy'].active:
                    self.change_animation('run_right')
            if self.x_direction == 'left':
                self.vel_x -= movement
                if not self.inair and not self.timers['light'].active and not self.timers['heavy'].active:
                    self.change_animation('run_left')
            if self.y_direction =='down' and self.inair:
                self.vel_y += y_movement

        #terminal fart
        if self.inair and self.vel_y < 7:
            self.vel_y += gravity
        if self.vel_x > 2:
            self.vel_x = self.vel_x
        
        self.vel_x = int(self.vel_x * friction)
        
        dy += self.vel_y
        dx += self.vel_x

        if self.timers['dodge_duration'].active:
            if self.x_direction == 'right':
                dx = dodge_vel
            elif self.x_direction == 'left':
                dx = -dodge_vel
            elif self.y_direction == 'up':
                dy = -dodge_vel
                self.vel_y = -1
            elif self.y_direction == 'down' and self.inair:
                dy = dodge_vel
                self.vel_y = 1

        if (self.timers['light'].active or self.timers['heavy'].active) and not self.inair and not self.timers['hit_duration'].active:
            self.change_animation('idle')
            dx = 0
            dy = 0
        
        for tile in tile_rects:
            if tile.colliderect(self.hitbox.x, self.hitbox.y + dy, self.hitbox.width, self.hitbox.height):
                if self.vel_y > 0:
                    dy = tile.top - self.hitbox.bottom
                    self.inair = False
                    self.jump_count = 0
                    self.change_animation('landing')
                if self.vel_y < 0:
                    dy = tile.bottom - self.hitbox.top
                self.vel_y = 0
            if tile.colliderect(self.hitbox.x + dx, self.hitbox.y, self.hitbox.width, self.hitbox.height):
                dx = 0
                self.vel_x = 0
                
        self.hitbox.y += int(dy)
        self.hitbox.x += int(dx)

    def check_dead(self):
        if self.hitbox.y < dead_top or self.hitbox.y > pygame.display.Info().current_h+dead_bottom:
            self.dead = True
        if self.hitbox.x > pygame.display.Info().current_w + dead_right or self.hitbox.x < dead_left:
            self.dead = True
    
    def update(self):
        self.timer_update()

        self.check_dead()
        
        #animation
        self.image = self.anim[self.frame]
        if self.timers['dodge_duration'].active:
            temp_image = self.image.copy()
            mask_surface = self.mask.to_surface(setcolor=(255, 255, 255, 0), unsetcolor=(0, 0, 0, 0))
            #fra chatgpt, basically mixer fargene sammen når man bruker blit. mixer hvit fra masken og original bildet
            temp_image.blit(mask_surface, (0, 0), special_flags=pygame.BLEND_RGB_ADD)
            self.image = temp_image
        if self.timers['special_anim_dur'].active:
            temp_image = pygame.Surface((self.hitbox.width, self.hitbox.height), pygame.SRCALPHA)
            self.image = temp_image
            
        self.rect.center = self.hitbox.center
        self.mask = pygame.mask.from_surface(self.image)
            
    
class Green(Characters):
    def __init__(self, group, attackgroup, spawnopposite=False):
        super().__init__(group, attackgroup, spawnopposite)
        #sprite sheets
        idle_sheet = load(join('assets', 'slime_sprites', 'PNG', 'Slime1', 'Without_shadow', 'Slime1_Idle_without_shadow.png')).convert_alpha()
        run_sheet = load(join('assets', 'slime_sprites', 'PNG', 'Slime1', 'Without_shadow', 'Slime1_Run_without_shadow.png')).convert_alpha()
        heavy_sheet = load(join('assets', 'slime_sprites', 'PNG', 'Slime1', 'Without_shadow', 'Slime1_Attack_without_shadow.png')).convert_alpha()
        
        #animation
        self.anim_list = {
            'idle': [self.get_image(i, idle_sheet, sprite_size, sprite_size, row=0) for i in range(6)],
            'run_right': [self.get_image(i, run_sheet, sprite_size, sprite_size, row=3) for i in range(8)],
            'run_left': [self.get_image(i, run_sheet, sprite_size, sprite_size, row=2) for i in range(8)],
            'jump': [self.get_image(i, run_sheet, sprite_size, sprite_size, row=0) for i in range(3)],
            'falling': [self.get_image(i, run_sheet, sprite_size, sprite_size, row=0) for i in range(3, 4)],
            'landing': [self.get_image(i, run_sheet, sprite_size, sprite_size, row=0) for i in range(4, 8)]
            }

        self.heavy_anim = {
            'side': [scale_by(pygame.transform.flip(load(join('assets', 'heavyattacks', 'shoot', 'SP401_nyknck', i)).convert_alpha(), True, False), 3) for i in listdir(join('assets', 'heavyattacks', 'shoot', 'SP401_nyknck'))],
            'up': [self.get_image(i, heavy_sheet, sprite_size, sprite_size, row=0) for i in range(10)],
            'down': [scale_by(load(join('assets', 'heavyattacks', 'down', 'SP201_nyknck', i)).convert_alpha(), 3) for i in listdir(join('assets', 'heavyattacks', 'down', 'SP201_nyknck'))],
            }
        
        self.anim = self.anim_list['idle']
        self.anim_steps = len(self.anim)

        max_rect = self.get_max_rect(self.anim_list)
        self.hitbox = pygame.Rect(0, 0, max_rect.width, max_rect.height)
        self.hitbox.topleft = self.spawn*cell_size
        self.hitbox.width -= 25
        self.hitbox.height -= 20
        
        self.image = self.anim[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = self.hitbox.center

        self.health = green_health

class Blue(Characters):
    def __init__(self, group, attackgroup, spawnopposite=False):
        super().__init__(group, attackgroup, spawnopposite)
        #sprite sheets
        idle_sheet = load(join('assets', 'slime_sprites', 'PNG', 'Slime2', 'Without_shadow', 'Slime2_Idle_without_shadow.png')).convert_alpha()
        run_sheet = load(join('assets', 'slime_sprites', 'PNG', 'Slime2', 'Without_shadow', 'Slime2_Run_without_shadow.png')).convert_alpha()
        heavy_sheet = load(join('assets', 'slime_sprites', 'PNG', 'Slime2', 'Without_shadow', 'Slime2_Attack_without_shadow.png')).convert_alpha()
        
        #animation
        self.anim_list = {
            'idle': [self.get_image(i, idle_sheet, sprite_size, sprite_size, row=0) for i in range(6)],
            'run_right': [self.get_image(i, run_sheet, sprite_size, sprite_size, row=3) for i in range(8)],
            'run_left': [self.get_image(i, run_sheet, sprite_size, sprite_size, row=2) for i in range(8)],
            'jump': [self.get_image(i, run_sheet, sprite_size, sprite_size, row=0) for i in range(3)],
            'falling': [self.get_image(i, run_sheet, sprite_size, sprite_size, row=0) for i in range(3, 4)],
            'landing': [self.get_image(i, run_sheet, sprite_size, sprite_size, row=0) for i in range(4, 8)]
            }

        self.heavy_anim = {
            'side': [scale_by(pygame.transform.flip(load(join('assets', 'heavyattacks', 'shoot', 'SP401_nyknck', i)).convert_alpha(), True, False), 3) for i in listdir(join('assets', 'heavyattacks', 'shoot', 'SP401_nyknck'))],
            'up': [self.get_image(i, heavy_sheet, sprite_size, sprite_size, row=0) for i in range(10)],
            'down': [scale_by(load(join('assets', 'heavyattacks', 'down', 'SP201_nyknck', i)).convert_alpha(), 3) for i in listdir(join('assets', 'heavyattacks', 'down', 'SP201_nyknck'))],
            }
        
        self.anim = self.anim_list['idle']
        self.anim_steps = len(self.anim)

        max_rect = self.get_max_rect(self.anim_list)
        self.hitbox = pygame.Rect(0, 0, max_rect.width, max_rect.height)
        self.hitbox.topleft = self.spawn*cell_size
        self.hitbox.width -= 25
        self.hitbox.height -= 35
        
        self.image = self.anim[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = self.hitbox.center

        self.health = blue_health

class Red(Characters):
    def __init__(self, group, attackgroup, spawnopposite=False):
        super().__init__(group, attackgroup, spawnopposite)
        #sprite sheets
        idle_sheet = load(join('assets', 'slime_sprites', 'PNG', 'Slime3', 'Without_shadow', 'Slime3_Idle_without_shadow.png')).convert_alpha()
        run_sheet = load(join('assets', 'slime_sprites', 'PNG', 'Slime3', 'Without_shadow', 'Slime3_Run_without_shadow.png')).convert_alpha()
        heavy_sheet = load(join('assets', 'slime_sprites', 'PNG', 'Slime3', 'Without_shadow', 'Slime3_Attack_without_shadow.png')).convert_alpha()
        
        #animation
        self.anim_list = {
            'idle': [self.get_image(i, idle_sheet, sprite_size, sprite_size, row=0) for i in range(6)],
            'run_right': [self.get_image(i, run_sheet, sprite_size, sprite_size, row=3) for i in range(8)],
            'run_left': [self.get_image(i, run_sheet, sprite_size, sprite_size, row=2) for i in range(8)],
            'jump': [self.get_image(i, run_sheet, sprite_size, sprite_size, row=0) for i in range(3)],
            'falling': [self.get_image(i, run_sheet, sprite_size, sprite_size, row=0) for i in range(3, 4)],
            'landing': [self.get_image(i, run_sheet, sprite_size, sprite_size, row=0) for i in range(4, 8)]
            }

        self.heavy_anim = {
            'side': [scale_by(pygame.transform.flip(load(join('assets', 'heavyattacks', 'shoot', 'SP401_nyknck', i)).convert_alpha(), True, False), 3) for i in listdir(join('assets', 'heavyattacks', 'shoot', 'SP401_nyknck'))],
            'up': [self.get_image(i, heavy_sheet, sprite_size, sprite_size, row=0) for i in range(10)],
            'down': [scale_by(load(join('assets', 'heavyattacks', 'down', 'SP201_nyknck', i)).convert_alpha(), 3) for i in listdir(join('assets', 'heavyattacks', 'down', 'SP201_nyknck'))],
            }
        
        self.anim = self.anim_list['idle']
        self.anim_steps = len(self.anim)

        max_rect = self.get_max_rect(self.anim_list)
        self.hitbox = pygame.Rect(0, 0, max_rect.width, max_rect.height)
        self.hitbox.topleft = self.spawn*cell_size
        self.hitbox.width -= 25
        self.hitbox.height -= 45
        
        self.image = self.anim[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = self.hitbox.center

        self.health = red_health


class Attacks(pygame.sprite.Sprite):
    def __init__(self, group, animinfo, duration, prect, adir, damage, knockback, heavy_attack = False, heavy_timer = False): #heavy_attacken er bare for spesial animasjoner
        super().__init__(group)
        self.animlist = animinfo[0]
        self.flip = animinfo[1]
        self.anim_steps = len(self.animlist)
        self.frame = 0
        self.prect = prect

        self.damage = damage
        self.knockback = pygame.Vector2(knockback)
        self.heavy_attack = heavy_attack
        
        self.image = pygame.transform.flip(self.animlist[0], self.flip, False)
        
        self.pos = self.prect.midbottom
        if adir == 'side' and heavy_attack == False:
            self.pos = (self.prect.centerx, self.prect.centery + 30)
        if adir == 'side' and heavy_timer:
            dirc = -1 if self.flip else 1
            self.pos = (self.prect.centerx + 70*dirc, self.prect.centery + 45)
        
        self.rect = self.image.get_rect(midbottom=self.pos)
        if self.heavy_attack:
            self.rect = self.image.get_rect(center=self.prect.center)
        
        #timers
        self.dur_timer = Timer(duration)
        self.dur_timer.activate()

        if heavy_attack or heavy_timer:
            self.frame_timer = Timer(heavy_attack_anim_speed, True, self.next_frame)
        else:
            self.frame_timer = Timer(attack_anim_speed, True, self.next_frame)
        self.frame_timer.activate()
        
    def next_frame(self):
        self.frame += 1
        if self.frame >= self.anim_steps:
            self.frame = self.anim_steps -1

    def update(self):
        self.frame_timer.update()
        self.dur_timer.update()
        
        self.image = pygame.transform.flip(self.animlist[self.frame], self.flip, False)
        self.rect = self.image.get_rect(midbottom=self.pos)
        self.mask = pygame.mask.from_surface(self.image)
        if self.heavy_attack:
            self.rect = self.image.get_rect(center=self.prect.center)
            self.image.set_colorkey('black')

        if not self.dur_timer.active:
            self.kill()

class Healthbar(pygame.sprite.Sprite):
    def __init__(self, group, health, pos):
        super().__init__(group)
        self.image = pygame.Surface((health_radius*2, health_radius*2), pygame.SRCALPHA)
        self.ratio = 0
        self.color = (255, 255, 255)
        pygame.draw.circle(self.image, 'black', (health_radius, health_radius), health_radius)
        pygame.draw.circle(self.image, self.color, (health_radius, health_radius), health_radius-health_border)
        self.pos = pygame.Vector2(pos)*cell_size
        self.rect = self.image.get_rect(center = self.pos)
        self.health = health

    def change(self, damage_taken):
        if damage_taken:
            ratio = damage_taken/self.health
            
            green = int((1-ratio)*255)
            
            if ratio >= 1:
                ratio = 2-ratio
                green = 0
            if ratio <= 0:
                ratio = 0
                green = 0
                
            red = int(ratio*255)
            
            self.color = (red, green, 0)
    
    def update(self):
        self.image.fill((0, 0, 0, 0))
        pygame.draw.circle(self.image, 'black', (health_radius, health_radius), health_radius)
        pygame.draw.circle(self.image, self.color, (health_radius, health_radius), health_radius-health_border)
        
