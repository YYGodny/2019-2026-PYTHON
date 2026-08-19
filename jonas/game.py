import time
import random
from collections import Counter

print('Skriv mine for å finne ting og skir inv for å se hva du har, skriv sell for å selge alt du har og skriv money for å se hvor mange penger du har')

money = 0
sa = 0
inv = ['Common_pickaxe']
a = dict(Counter(inv))
icount = 0
dcount = 0

while True:
    pi = input()
    if pi == 'mine':
        a = random.randint(0, 3)
        if a == 0:
            print('Du fant ingenting.')
        elif a == 1:
            print('Du fant en Iron ore!')
            inv.append('Iron_ore')
            icount += 1
        else:
            print('Du fant Diamonds!')
            inv.append('Diamond')
            dcount += 1
    elif pi == 'inv':
        print(inv)
    elif pi == 'sell':
        inv.remove('Common_pickaxe')
        a = dict(Counter(inv))
        sa = icount*5 + dcount*10
        print(a, 'solgt for', sa, '$')
        inv.clear()
        inv.append('Common_pickaxe')
        money += sa
        sa = 0
    elif pi == 'money':
        print(money, '$')
