import pygame
import json
from os.path import join

cell_size = 32
rows = 22
columns = 33

map_width = 1056
map_height = 704

gravity = 1
jump = -16
movement = 3
y_movement = 2
offset = 10
friction = 0.7
dodge_cooldown = 3000
dodge_vel = 10
dodge_duration = 200
hit_duration = 100

LIGHT = 300
HEAVY = 1000
light_cooldown = 550
heavy_cooldown = 1000

light_damage = {
    'side': 4,
    'up': 3,
    'down': 2,
    }

light_knockback = {
    'side': (10, -1),
    'up': (0, -6),
    'down': (5, -4),
    }

heavy_damage = {
    'side': 8,
    'up': 10,
    'down': 5,
    }

heavy_knockback = {
    'side': (15, -3),
    'up': (7, -7),
    'down': (6, -4),
    }

animation_time = 100
attack_anim_speed = 30
heavy_attack_anim_speed = 100
sprite_size = 64

health_radius = 20
healthpos1 = (2, 2)
healthpos2 = (38, 2)
blue_health = 120
green_health = 150
red_health = 100
health_border = 3

dead_top = -600
dead_bottom = 100
dead_left = -100
dead_right = 100

#tilemap
with open(join('assets', 'map1.json'), 'r') as f:
    TILE_DATA = json.load(f)['layers'][0]['data2D']
    
