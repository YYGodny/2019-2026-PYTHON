def pfil(fil):
    for i in fil:
        print(i.strip())

with open('foroppgaver.txt', 'r+') as f:
    text = f.readlines()
    pfil(text)
    while True:
        ønske = input('legg til ønske: ')
        if ønske.upper() == 'STOPP':
            pfil(text)
            break
        f.write(f'{ønske}\n')
        text.append(f'{ønske}\n')
    print('skriv rekkefølgen:')
    rekkefølge = []
    for index, item in enumerate(text):
        r = input(f'nr{index}: ')
        rekkefølge.append(f'{r}\n')
    f.seek(0)
    f.writelines(rekkefølge)
    f.seek(0)
    pfil(f.readlines())

def sønske(ønske):
    with open('foroppgaver.txt', 'r+') as f:
        t = f.readlines()
        t.remove(f'{ønske}\n')
        f.seek(0)
        f.writelines(t)
