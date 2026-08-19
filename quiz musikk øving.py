import random
import time
from PIL import Image
import os
import pyautogui

poeng = 0
def få_ord(x, få=False):
    x = x.split(' ')
    if få == True:
        return len(x), x
    return len(x)

def riktig_svar(b, svar, x, alt='no'):
    global poeng
    riktige_ord = []
    riktig_poeng = 0
    if alt != 'no':
        ixalt2, italt2 = få_ord(b[x][alt], få=True)
    elif alt == 'no':
        ixalt2, italt2 = få_ord(b[x], få=True)
    lengsvar, ordsvar = få_ord(svar, få=True)
    if ordsvar == italt2:
        poeng += ixalt2
        riktig_poeng = ixalt2
        print('helt riktig!')
        return riktig_poeng
    try:
        for index, item in enumerate(italt2):
            if ordsvar[index] == item:
                poeng += 1
                riktig_poeng += 1
                riktige_ord.append(item)
        print(f'riktig svar: {italt2}')
        print(f'det du fikk riktig: {riktige_ord}')
        return riktig_poeng
    except:
        print(f'riktig svar: {italt2}')
        print(f'det du fikk riktig: {riktige_ord}')
        return riktig_poeng
    
def begreper():
    global poeng
    b = {'synkope' : ['i en 4/4 takt er det 4 grunnslag på hver fjerdedel. Imellom disse kan det spilles, synges, eller danses en synkopert rytme.', 'slag som ikke er på slaget'],
         'perkusjon' : 'Perkusjon er en fellesbetegnelse på diverse slagverkinstrumenter.',
         'Vekselsang/call and response' : 'noen synger noe, andre svarer syngende.',
         'Polyrytmer' : 'flere rytmer sammen',
         'backbeat' : 'slag på det andre og fjerde slaget i en 4/4 takt, som er slepende/bakpå',
         'shruti' : 'den indiske skalaen er inndelt i 22 shruti (toner). Tone skalaen til indisk musikk.',
         'raga' : 'en kombinasjon av 5-7 toner',
         'verdensmusikk' : 'tradisjonell folkemusikk fra hele verden, ofte blandet med elementer fra vestlig populær-musikk'
        }
    for index, item in enumerate(b):
        key, val = random.choice(list(b.items()))
        print('hva er', key)
        svar = input('svar: ')
        riktig_poeng = 0
        if key == 'synkope':
            riktige_ord = []
            ixalt2, italt2 = få_ord(b['synkope'][1], få=True)
            lengsvar, ordsvar = få_ord(svar, få=True)
            if lengsvar <= ixalt2 or lengsvar + 2 <= ixalt2:
                if ordsvar == italt2:
                    poeng += ixalt2
                    riktig_poeng = ixalt2
                    print('helt riktig!')
                    print(f'også:', b['synkope'][0])
                else:
                    try:
                        for index, item in enumerate(italt2):
                            if ordsvar[index] == item:
                                poeng += 1
                                riktig_poeng += 1
                                riktige_ord.append(item)
                            else:
                                continue
                        print('riktig svar: {italt2}')
                    except:
                        pass
            elif lengsvar > ixalt2 + 2:
                riktig_poeng = riktig_svar(b, svar, 'synkope', alt=0)
            
            if len(riktige_ord) > 0:
                print(riktige_ord)
            
        if key == 'perkusjon':
            riktig_poeng = riktig_svar(b, svar, 'perkusjon')
            if 'for eksempel' in svar or 'for eks.' in svar:
                if 'cajon' in svar:
                    riktig_poeng +=1
                    poeng += 1
                if 'tromme' in svar:
                    riktig_poeng +=1
                    poeng += 1
                if 'triangel' in svar:
                    riktig_poeng +=1
                    poeng += 1
                if 'claves' in svar:
                    riktig_poeng +=1
                    poeng += 1
        if key == 'Vekselsang/call and response':
            riktig_poeng = riktig_svar(b, svar, 'Vekselsang/call and response')
        if key == 'Polyrytmer':
            riktig_poeng = riktig_svar(b, svar, 'Polyrytmer')
        if key == 'backbeat':
            riktig_poeng = riktig_svar(b, svar, 'backbeat')
        if key == 'shruti':
            riktig_poeng = riktig_svar(b, svar, 'shruti')
        if key == 'raga':
            riktig_poeng = riktig_svar(b, svar, 'raga')
        if key == 'verdensmusikk':
            riktig_poeng = riktig_svar(b, svar, 'verdensmusikk')
        
        print(f'+{riktig_poeng}!')
        print('poeng: ', poeng)
                    
def instrumenter():
    global poeng
    directory = r'C:\Users\fipha001\Pictures\instrumenter'
    navn = {}
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        navn[f] = filename
    for filename in os.listdir(directory):
        key, val = random.choice(list(navn.items()))
        navn.pop(key)
        im = Image.open(key)
        im.show()
        val = val.split('-')
        inst = True
        while inst:
            svar = input('hvilket instrument er dette: ')
            if svar == val[0]:
                print('riktig!')
                poeng += 1
                inst = False
            else:
                print('feil')
        land = True
        while land:
            svar = input('hvor kommer det fra: ')
            if '.png' in val[1]:
                g = val[1].split('.png')
            if '.jpg' in val[1]:
                g = val[1].split('.jpg')
            if svar == g[0]:
                print('riktig')
                poeng += 1
                pyautogui.click(1346, 7)
                land = False
            else:
                print('feil')

def sjanger_historie_kjennetegn():
    global poeng
    pass

def blandet():
    global poeng
    pass

while True:
    poeng = 0
    x = input('hvilket tema vil du ha? (skriv 1, 2,3 eller 4):\n1. begreper\n2. instruementer\n3. sjanger, kjennetegn og historie\n4. blandet\n')
    if x == '1':
        begreper()
    if x == '2':
        instrumenter()
    print('DU FIKK', poeng)
    
