#for i in range(1, 20, 2):
#    print(i)

#l = float(input('skriv lengde: '))
#b = float(input('skriv bredde: '))
#print(l*b)


from pylab import *

n = 100
gunstig = 0

for i in range(n):
    terning1 = randint(1, 7)
    terning2 = randint(1, 7)
    if terning1 + terning2 >= 4:
        gunstig += 1
        
print('relativ frekvens: ', gunstig/n)