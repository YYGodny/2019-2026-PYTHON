import random

typer = ['troll', 'gnom', 'heks', 'alv', 'varulv', 'tyv']
adjektiv = ['stygg', 'pen', 'rasende', 'hårete', 'fredelig']

class boss:
    def __init__(self, aktiv):
        self.aktiv = aktiv
        if aktiv == True:
            self.dead = False
            self.health = random.randint(90, 130)
            self.armour = random.randint(10, 30)
            self.attack = random.randint(35, 50)
            self.speed = random.randint(70, 90)
sjef = ()

def get_boss():
    global sjef
    sjef = boss(True)
    monster = random.choice(typer)
    beskrivelse = random.choice(adjektiv)
    print(f'du fant en {beskrivelse} {monster}!')
    print(f'STATS: ATTACK:{sjef.attack}, ARMOUR:{sjef.armour}, HEALTH:{sjef.health}, SPEED:{sjef.speed}')


def attack(mot, fra):
    mot.health -= fra.attack
    
    
#def stats():
#    print(sjef.aktiv, sjef.health, sjef.armour, sjef.attack, sjef.speed)
