import csv
import json

##
##with open(r'C:\Users\fipha001\Downloads\filer eksamen h25 datasett\Elever-fag.csv', 'r+', encoding='Windows-1252') as f:
##    file = csv.reader(f, delimiter=',')
##    tittel = next(file)
##    for i in file:
##        print(i)


fagområder = {}

with open(r'C:\Users\fipha001\Downloads\filer eksamen h25 datasett\Elever-fag.json', encoding='Windows-1252') as f:
    file = json.load(f)
    for i in file:
        if not i['Fagomraadenavn'] in fagområder:
            fagområder[i['Fagomraadenavn']] = [0, 0, 0]
        for index, item in enumerate(list(i.values())[3::]):
            if item != None:
                fagområder[i['Fagomraadenavn']][index] += int(item.replace(' ', ''))
##        fagområder[i['Fagomraadenavn']] += sum([int(år.replace(' ', '')) for år in list(i.values())[3::] if år != None])
    
    print('oppgave a \n')
    for i in fagområder:
        print(f'{i}: {fagområder[i]}')

    print('\n\noppgave b')   
    for i in fagområder:
        print(i)
        
    f = input('Velg et fagområde: ')

    fag = []
    for i in file:
        if i['Fagomraadenavn'] == f:
            fag.append(i['Opplaeringsfagnavn'])

    print(f, set(fag))
