import random

class Hat:
    def __init__(self, **balls):
        [int(i) for i in balls.values()]

        self.contents = []
        for ball in balls:
            [self.contents.append(ball) for i in range(balls[ball])]


    def draw(self, numofballs):
        self.drawn = []
        if numofballs > len(self.contents):
            [self.drawn.append(i) for i in self.contents]
            self.contents = []
        else:
            for i in range(numofballs):
                r = random.randint(0, len(self.contents))
                self.drawn.append(self.contents[r])
                self.contents.pop(r)
        return self.drawn
