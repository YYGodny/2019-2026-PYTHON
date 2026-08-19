#fighting, achivements, stats, dø, inventory
import time
import random
import boss_generator, fight

print('du kan skrive finn loot, bruk + (loot navn), explore, inventory, stats og finn boss for å gjøre ting.')

inventory = []
spiller = True

andreas_sin_promp = {
    'type' : 'sverd',
    'rare' : False,
    'damage' : 5,
    'navn' : 'andreas sin promp'
}
   
filip_sitt_sverd = {
    'type' : 'sverd',
    'rare' : True,
    'damage' : 25,
    'navn' : 'filip sitt sverd'
}


    

class person:
    def __init__(self, name):
        self.attack = random.randint(20, 31)
        self.armor = 0
        self.health = random.randint(20, 31)
        self.speed = random.randint(20, 31)
        self.dead = False

    def die(self):
        global spiller
        self.dead = True
        print('GAME OVER!')
        spiller = False
        
    def stats(self):
        print(f'din attack er {self.attack} din armor er {self.armor} din health er {self.health} din speed er {self.speed}')

player1 = person('Filip')


def explore():
    print('du møter en hjemløs mann som heter andreas hva gjør du?')
    x = input()
    if len(x) > 0:
        print(f'du prøver å {x}')
    success = random.randint(1, 5)
    if success != 3:
        print('success!')
        print('ARMOUR + 1, HEALTH + 1, SPEED + 1, ATTACK +1')
        player1.attack += 1
        player1.armor += 1
        player1.health += 1
        player1.speed += 1
    else:
        player1.health -= 12
        print('han løp')
        print('du tok 12 damage')

    
def boss():
    print(end='leter etter boss')
    time.sleep(.5)
    print(end='.')
    time.sleep(.5)
    print(end='.')
    time.sleep(.5)
    print('.')
    
    #drage = int(random.randint(3, 10))
    #trollmann = int(random.randint(11, 16))
    #black_man = int(random.randint(20, 30))
    random_boss = int(random.randint(31, 35))

    '''
    if drage == 6:

        drage = True
        print('du fant en stor rød drage!')
        time.sleep(.5)
        print('1.prompe i munnen hans')
        time.sleep(.5)
        print('2.knyte et tau rundt han')
        time.sleep(.5)
        print('3.kniv stikke han')
        #fight.fight(drage, player1)
            
    elif trollmann == 14:
        trollmann = True
        print('du fant en ensom trollman som heter lavrans!')
        #fight.fight(trollmann, player1)
        
    elif black_man == 25:
        black_man = True 
        print('du fant en svart man som har en kniv!')
        #fight.fight(black_man, player1)
    '''    
    if random_boss == 33:
        random_boss = True
        boss_generator.get_boss()
        fight.fight(random_boss, player1, boss_generator.sjef)
        
    else:
        print('du fant ingen boss')
    
    
    
def bruk(x):
    y = x['type']
    if y == 'sverd':
        y = x['damage']
    player1.attack += y
    print(f'du bruker: ', x['navn'])
    
    



def let_etter_loot():
    rare_loot = random.randint(1, 25)
    loot = random.randint(1, 3)
    if rare_loot == 14:
        inventory.append(filip_sitt_sverd)
        print('DU FANT RARE LOOT!: filip sitt sverd')
    if loot == 2:
        inventory.append(andreas_sin_promp)
        print('du fant dårlig loot: andreas sin promp')
    else:
        print('du fant ingen ting')
        
        
    

        
    
while spiller:
    try:
        svar = input()
        if 'finn loot' in svar:
            let_etter_loot()
        elif 'explore' in svar:
            explore()
        elif 'inventory' in svar:
            print(inventory)
        elif 'finn boss' in svar:
            boss()
        elif 'stats' in svar:
            player1.stats()
        elif 'bruk andreas sin promp' in svar:
            bruk(andreas_sin_promp)
        elif 'bruk filip sitt sverd' in svar:
            bruk(filip_sitt_sverd)
        else:
            print('jeg tror du skrev noe feil')
    except:
        print('det skjedde noe feil og nå dør jeg')
