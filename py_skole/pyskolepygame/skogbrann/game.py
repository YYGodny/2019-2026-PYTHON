from settings import *

class Game:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.matrix = [[0 for col in range(cols)] for row in range(rows)]

        self.timers = {
            'plant_tree': Timer(plant_time, True, self.plant_tree),
            'spawn_lyn': Timer(lyn_time, True, self.spawn_lyn),
            'brenn': Timer(brenn_time, True, self.check_burning),
            }
        self.timers['plant_tree'].activate()
        self.timers['spawn_lyn'].activate()
        self.timers['brenn'].activate()

    def make_grid(self):
        for row in range(1, rows):
            pygame.draw.line(self.display_surface, 'gray', (0, row*cell_size), (window_width, row*cell_size), 1)
        for col in range(1, cols):
            pygame.draw.line(self.display_surface, 'gray', (col*cell_size, 0), (col*cell_size, window_height), 1)

    def draw_trees(self):
        for yindex, row in enumerate(self.matrix):
            for xindex, item in enumerate(row):
                if item == 1:
                    pygame.draw.rect(self.display_surface, 'green', (xindex*cell_size, yindex*cell_size, cell_size, cell_size))
                if item == 2:
                    pygame.draw.rect(self.display_surface, 'red', (xindex*cell_size, yindex*cell_size, cell_size, cell_size))
                if item == 3:
                    pygame.draw.rect(self.display_surface, 'yellow', (xindex*cell_size, yindex*cell_size, cell_size, cell_size))

    def plant_tree(self):
        for yindex, row in enumerate(self.matrix):
            for xindex, item in enumerate(row):
                if random.choice([1, 2, 3, 4]) == 1 and item == 0:
                    self.matrix[yindex][xindex] = 1

    def spawn_lyn(self):
        for yindex, row in enumerate(self.matrix):
            for xindex, item in enumerate(row):
                if random.randint(1, 100) <= 3 and item == 1:
                    self.matrix[yindex][xindex] = 2
                    self.timers['plant_tree'].deactivate()
                    self.timers['spawn_lyn'].deactivate()
                    self.timers['spawn_lyn'].repeated = False
                    return
                    
    def timer_update(self):
        for i in self.timers.values():
            i.update()

    def check_burning(self):
        burning = False
        for row, _ in enumerate(self.matrix):
            for col, item in enumerate(_):    
                if item == 1:
                    top = [(col+i,row-1) for i in [-1, 0, 1]]
                    lr = [(col+i, row) for i in [-1, 1]]
                    bottom = [(col+i, row+1) for i in [-1, 0, 1]]
                    items = top+lr+bottom
                    joe = []
                    for i in items:
                        if 0 <= i[0] < len(self.matrix[0]) and 0 <= i[1] < len(self.matrix):
                            joe.append(i)
                    
                    items = [self.matrix[i[1]][i[0]] for i in joe]
                    
                    if 2 in items:
                        self.matrix[row][col] = 3
                        
                if item == 2:
                    self.matrix[row][col] = 0
                
                if item == 3:
                        self.matrix[row][col] = 2
                        
                    
        for i in self.matrix:        
            if 2 in i or 3 in i:
                burning = True
                
        if not burning and not self.timers['plant_tree'].active and not self.timers['spawn_lyn'].active:
            self.timers['plant_tree'].repeated = True
            self.timers['plant_tree'].activate()
            self.timers['spawn_lyn'].repeated = True
            self.timers['spawn_lyn'].activate()
            
        if burning:
            self.timers['plant_tree'].repeated = False
            self.timers['plant_tree'].deactivate()
            self.timers['spawn_lyn'].repeated = False
            self.timers['spawn_lyn'].deactivate()
            
    def run(self):
        self.make_grid()
        self.timer_update()
        self.draw_trees()
