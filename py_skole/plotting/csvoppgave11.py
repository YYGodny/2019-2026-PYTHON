import csv
import matplotlib.pyplot as plt

xverdier = []
yverdier = []

with open('12952_20251017-144057.csv', encoding='UTF-8') as f:
    innhold = csv.reader(f, delimiter=';')
    overskrift = next(innhold)[0]
    for index, item in enumerate(innhold):
        if index > 3:
            xverdier.append(item[0])
            yverdier.append(item[1])

plt.bar(xverdier, list(map(int,yverdier)))
plt.title(overskrift)
plt.show()
