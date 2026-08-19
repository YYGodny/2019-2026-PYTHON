import random
import time

def hei():
    return('hei')


class testdukke:
    def __init__(self, attack, health):
        self.attack = attack
        self.health = health
        
helt = testdukke(60, 100)

class testdukkeskurk:
    def __init__(self, health, attack):
        self.health = health
        self.attack = attack
        
skurk = testdukkeskurk(100, 101)

def fight(aktiv, egenstat, motstander):
    print('hva skal du gjøre?')
    time.sleep(.5)
    print('skriv kast terning etter at du har svart!')
    time.sleep(.5)
    unlucky_number = random.randint(1, 6)
    print(f'det uheldige sifferet er {unlucky_number}!')

    while aktiv:
        
        while True:
            svar = input('attack: ')
            if 'kast terning' in svar:
                print('ikke skriv kast terning nå')
                
            elif len(svar) <= 5:
                print('jeg tror du skrev noe feil')
                
            else:
                break
            
        terning = random.randint(1, 6)
        
        while True:
            kast_terning = input('terning: ')
            if 'kast terning' in kast_terning:
                time.sleep(.5)
                print(terning)
                time.sleep(.5)
                break
            else:
                print('skriv kast terning!')
        
        
        if unlucky_number == terning:
            print('DU BOMMA!')
            egenstat.health -= motstander.attack
            if egenstat.health <= 0:
                egenstat.die()
                break
            print(f'DU TOK {motstander.attack} damage\nDIN HEALTH ER [{egenstat.health}]')

        else:
            print('DET FUNKA!')
            motstander.health -= egenstat.attack
            if motstander.health > 0:
                print(f'BOSSEN SIN HEALTH ER [{motstander.health}]!')
            else:
                print('DU SLO HAN!!!')
                aktiv = False
        
        
        
    
