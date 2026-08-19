import csv
import matplotlib.pyplot as plt
import numpy as np

with open('slakt_tonn.csv', encoding='UTF-8') as f:
    a = csv.reader(f, delimiter=';')

    #oppgave a
    overskrifter = next(a)
    for index, item in enumerate(overskrifter):
        if item == '2017':
            index2018 = index
    for i in a:
        if i[0][3::].upper() == 'ROGALAND':
            if i[1].upper() == 'STORFE':
                print(i[index2018])
        if i[0][3::].upper() == 'BUSKERUD':
            if i[1].upper() == 'STORFE':
                print(i[index2018])

    #oppgave b
    f.seek(0)
    x = []
    y = []
    for i in a:
        if i[0][3::].upper() == 'HEDMARK':
            x.append(i[1])
            y.append(sum(map(int, i[2::])))
    plt.barh(x, y)
    plt.show()

    #oppgave c
    f.seek(0)
    fylker = []
    fylke = [0 for i in range(17)]
    next(a)
    for index, item in enumerate(a):
        for ix, it in enumerate(item[2::]):
            fylke[ix] += int(it)
        if index != 0 and index % 5 == 0:
            fylker.append(fylke)
            fylke = [0 for i in range(17)]
    f.seek(0)
    xnavn = list(set([i[0] for i in a]))[1::]
    x = np.arange(2001, 2018)
    farger = [
    "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown",
    "black", "white", "gray", "cyan", "magenta", "lime", "teal", "lavender",
    "maroon", "navy"
    ]
    #fra copilot#####
    bar_width = 0.8 / len(xnavn)  # bredde per fylke

    for index, item in enumerate(xnavn):
        offset = index * bar_width
        plt.bar(x + offset, fylker[index], width=bar_width, color=farger[index], label=item)

    plt.xticks(x + bar_width * (len(xnavn) / 2), x)  # sentrer årstallene
    plt.legend()
    plt.show()
