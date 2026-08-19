import random
import time

tries = 0
l = False
h = False

def ask():
    global tall, tries, l, h

    while True:
        x = input('ja/higher/lower')
        x = x.replace(' ', '')
        x = x.lower()
        tries += 1

        if x == 'ja':
            print(f'Jeg brukte {tries} tries!')
            break
        elif x == 'lower':
            l = True
            tall -= 5
        elif l == True and x == 'higher':
            tall += 1
        elif x == 'higher':
            h = True
            tall += 5
        elif h == True and x == 'lower':
            tall -= 1
        print(f'Er det {tall}?')
    
while True:
    print('Tenk på et tall mellom 0 og 100')
    time.sleep(1)
    print('5')
    time.sleep(1)
    print('4')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('0')
    print('Nå skal jeg gjette!')
    time.sleep(1)
    
    tall = 50
    print(f'Er det {tall}?')
    ask()
    break
