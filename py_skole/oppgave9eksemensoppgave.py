import csv
import matplotlib.pyplot as plt

'''
jeg liker mat
jeg liker mat
'''

with open(r'C:\Users\fipha001\Downloads\filer eksamen h24 datasett\filer eksamen h24 datasett\Datasett_fodselstall_komma(1).csv', encoding='utf-8') as f:
    file = csv.reader(f, delimiter=',')
    overskrift = next(file)
    print(overskrift)
    datacolnavn = ["fødselstall", "innflyttinger", "utflyttinger", "netto folkevekst"]
    datarownavn = []
    data = []
    for i in file:
        
    for i in file:
        data.append([int(y) if y != '' else 0 for y in i])
    for i in data:
        i[1] = i[0]+i[2]-i[3]
   
    
    
    table = plt.table(cellText=data, colLabels=datacolnavn, loc='center')

    plt.axis('off')
    plt.show()
