import csv
import matplotlib.pyplot as plt

with open('friluftsaktiviteter.csv', encoding='UTF-8') as f:
    a = csv.reader(f, delimiter=';')
    overskrifter = next(a)
    #oppgave 8a
    with open('oppgave8tabell.csv', 'w') as f2:
        for i in a:
            f2.write(f'{i[0]};{sum((map(int, i[1::])))}\n')

    while True:             
        #oppgave 8b
        fylker = [i.replace('1 000 personer 2024 ', '')[3:] for i in overskrifter]
        for i in fylker[1:]:
            print(i)
        valgtfylke = input('skriv et fylke: ')
        for index, item in enumerate(fylker):
            if item.upper() == valgtfylke.upper():
                fylkeindex = index
                
        f.seek(0)
        fylkeaktiviteter = {}
        for index, item in enumerate(a):
            if index >= 1:
                fylkeaktiviteter[item[0]] = int(item[fylkeindex])
                
        sortedfylkeaktiviteter = sorted(fylkeaktiviteter.items(), key=lambda x:x[1])
        fylkeaktiviteter = dict(sortedfylkeaktiviteter)
        
        for i in fylkeaktiviteter:
            print(i, fylkeaktiviteter[i])

        print('\n\nPROSENTDEL\n\n')
        
        for i in fylkeaktiviteter:
            print(i, f'{fylkeaktiviteter[i]/10}%')

        
        #oppgave 8c
        x = []
        y = []
        for index, item in enumerate(reversed(fylkeaktiviteter)):
            if index < 3:
                x.append(item)
                y.append(fylkeaktiviteter[item])
        plt.barh(x, y)
        plt.show()
        

            
    
    
        
