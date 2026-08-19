import csv
import matplotlib.pyplot as plt

with open('Datasett_fodselstall_komma.csv', 'r+') as f:
    #oppgave 1
    fil = csv.reader(f, delimiter=',')
    overskrift = next(fil)
    print(overskrift)
    x = [int(i[0]) for i in fil]
    f.seek(0)
    next(f)
    y = [int(i[1]) for i in fil]
    
    plt.plot(x, y)
    plt.show()

    #oppgave 2
    f.seek(0)
    data = csv.reader(f,delimiter=',')
    next(data)
    overskrifter = overskrift[1::]
    overskrifter.append('netto folkevekst')
    d = [i[1::] for i in data]
    for i in d:
        if i[0] == '':
            i[0] = 0
        if i[1] == '':
            i[1] = 0
        if i[2] == '':
            i[2] = 0
        i.append(int(i[0]) + int(i[1]) - int(i[2]))
    plt.table(cellText = d,
              rowLabels= x,
              colLabels= overskrifter)

    plt.axis('off')
    plt.show()

    
