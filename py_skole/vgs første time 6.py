while True:
    x = int(input('skriv et heltall'))
    if x % 2 == 0:
        print(f'{x} er et partall')
        continue
    if True not in [x % (i+2) == 0 for i in range(x-2)]:
        print(f'{x} er et primtall')
        continue
    else:
        print(f'{x} er et oddetall')
        
