import random
import time
import sys

ord1 = ['eple', 'kake', 'ost', 'muggost', 'femtifire', 'jonas', 'gay', 'bitch']

def ny():
    x = input('Vil du starte på nytt?')
    if x.lower() == 'ja':
        game()
    if x.lower() == 'nei':
        sys.exit()
    
def game():
    ord2 = random.choice(ord1)
    tries = ['♥', '♥', '♥', '♥', '♥', '♥', '♥', '♥', '♥', '♥']
    p = 9
    riktig = []
    for i in ord2:
        riktig.append('_')
    while True:
        u = False
        for i in ord2:
            print(end='_')
            
        x = input('\nGjett en boktsav eller et ord')
        for index, item in enumerate(ord2):
            if x == item and x not in riktig:
                riktig[index] = x
                u = True

        q = ''.join(riktig)
        print(q)
        if q == ord2:
            print('Du gjetta ordet!')
            ny()
        if u == False:    
            p -= 1
            tries.pop(p)
        tries2 = ' '.join(tries)
        print(tries2)
        if tries == []:
            print('DU TAPTE NOOB!')
            print(f'ORDET VAR {ord2}!')
            ny()
        
if __name__ == '__main__':
    game()
