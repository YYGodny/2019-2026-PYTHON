# Write your code here :-)
from pylab import *
print('Programmet skal løse andregradslikningen')
print('ax^2 + bx + c = 0 ved hjelp av abc-formelen.')
print('Skriv inn verdiene for a, b og c.')

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

d = b**2 - 4*a*c
if d < 0:
    print('uløselig')
else:
    x1 = (-b + sqrt(d))/(2*a)
    x2 = (-b - sqrt(d))/(2*a)

if d > 0:
    print('løsningen på andregradslikningen er:')
    if x1 == x2:
        print(f'x = {round(x1, 2)}')
    else:
        print('x1 =', round(x1, 2), 'og x2 =', round(x2, 2))
