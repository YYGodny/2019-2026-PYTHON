'''
def areal_sirkel(r):
    return 3.14*r*r

print(areal_sirkel(3))

def areal_trekant(h, gl):
    return (h*gl)/2

print(areal_trekant(3, 4))

def hypotenus(a, b):
    return (a*a + b*b)**(1/2)

print(hypotenus(3, 4))

'''



alphabet = "abcdefghijklmnopqrstuvwxyzæøå"

letter = "a"
key = 3

pos = alphabet.find(letter)

newpos = (pos + key)

if newpos >= 29:
    newpos = newpos - 29

secretletter = alphabet[newpos]

print(secretletter)




































