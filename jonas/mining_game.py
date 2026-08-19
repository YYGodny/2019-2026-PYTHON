import time
import random
from collections import Counter
from tqdm import tqdm

print('Skriv mine for å finne ting og skriv inv for å se hva du har, skriv sell for å selge alt du har, skriv money for å se hvor mange penger du har og skriv store for å kjøpe nye pickaxer')

money = 0
sa = 0
inv = ['Wooden_pickaxe']
oreinv = {}
icount = 0
dcount = 0
solgt = 0
pickaxes = ['Stone_pickaxe 100$', 'Iron_pickaxe 300$', 'Diamond_pickaxe 750$', 'Netherite_pickaxe 1500$']
ores = {
    'Ingenting': 0,
    'Stone': 5,
    'Iron': 10,
    'Gold': 13,
    'Diamonds': 20,
    'Netherite': 35
    }
pickore = ['Ingenting', 'Stone', 'Iron', 'Gold', 'Diamonds', 'Netherite']
weights = [1250, 1000, 750, 550, 325, 100]
current_p = inv[0]

while True:
    pi = input()

    if pi == 'mine':
        a = random.choices(pickore, weights=weights)[0]
        if a == 'Ingenting':
            print('Du fant ingenting :(')
            continue
        for i in tqdm(range(ores[a])):
            time.sleep(0.1)
        
        print('Du fant {}'.format(a))
        if a not in oreinv:
            oreinv[a] = 1
        else:
            oreinv[a] += 1

    elif pi == 'inv':
        print(inv)
        print(oreinv)

    elif pi == 'sell':
        sa = 0
        for a, n in oreinv.items():
            sa += ores[a] * n
            oreinv[a] = 0
        icount = 0
        dcount = 0
        money += sa
        print('solgt for', sa, '$')
        sa = 0
        inv.clear()
        inv.append(current_p)

    elif pi == 'money':
        print(money, '$')

    elif pi == 'store':
        print(pickaxes)
        print('Skriv hvilken pickaxe du vil kjøpe for eksempel "iron", skriv "cancel" for å avbryte')
        si = input()
        if si == 'stone':
            if money >= 100:
                money -= 100
                inv.remove(current_p)
                current_p = 'Stone_pickaxe'
                inv.append(current_p)
                print('Du kjøpte Stone pickaxe for 100$')
            else:
                print('Du har ikke råd til denne pickaxen')
                
        elif si == 'iron':
            if money >= 300:
                money -= 300
                inv.remove(current_p)
                current_p = 'Iron_pickaxe'
                inv.append(current_p)
                print('Du kjøpte Iron pickaxe for 300$')
            else:
                print('Du har ikke råd til denne pickaxen')

        elif si == 'diamond':
            if money >= 750:
                money -= 750
                inv.remove(current_p)
                current_p = 'Diamond_pickaxe'
                inv.append(current_p)
                print('Du kjøpte Diamond pickaxe for 750$')
            else:
                print('Du har ikke råd til denne pickaxen')

        elif si == 'netherite':
            if money >= 1500:
                money -= 1500
                inv.remove(current_p)
                current_p = 'Netherite_pickaxe'
                inv.append(current_p)
                print('Du kjøpte Netherite pickaxe for 1500$')
            else:
                print('Du har ikke råd til denne pickaxen')

        elif si == 'cancel':
            print('Store lukket')
