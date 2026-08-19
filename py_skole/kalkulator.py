running = True
while running:
    try:
        t1 = float(input('skriv inn et tall: '))
        r = input('skriv en regneoperatsjon: ')
        t2 = float(input('skriv inn tall2: '))
        if r == '/' or r ==':':
            print(t1/t2)
        elif r == '+':
            print(t1+t2)
        elif r == '-':
            print(t1-t2)
        elif r == '*':
            print(t1*t2)
        elif r == '%':
            print((t1/100)*t2)
        else:
            print('ugyldig regneoperasjon')
    except:
        print('du skrev noe feil')
        running = True
