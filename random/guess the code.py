import random

code = random.randint(1000, 10000)

code2 = str(code)
tries = 10

print(code)
while True:
    x = str(input('\nEnter your four digit guess code: '))
    tries -= 1
    list1 = []
    if len(x) == 4:
        for index, item in enumerate(x):
            if item not in code2:
                list1.append('B')
            elif item in code2 and item != code2[index]:
                list1.append('Y')
            elif item == code2[index]:
                list1.append('R')
        a = ''.join(list1)
        if a == 'RRRR':
            print(f'You guessed it! {code}')
            break
        if tries <= 0:
            print(f'You lost!')
            break
        print(f'You have {tries} tries left')
        print(a)
    else:
        print('Du må skrive et annet tall')
    
