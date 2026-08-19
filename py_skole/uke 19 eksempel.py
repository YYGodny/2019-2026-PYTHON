'''
#Program som regner ut areal og omkrets av rektangler
lengde = input("oppgi lengde i cm: ")
bredde = input("oppgi bredde i cm: ")
lengde = float(lengde)
bredde = float(bredde)
 
areal = lengde * bredde
omkrets = lengde*2 + bredde*2
 
print("arealet er", areal, "cm2", 'omkretsen er:', omkrets, 'cm')
'''




#oppgave 1:
for i in range(2, 21, 2):
    print(i)

#oppgave 2 og ekstra oppgave:
r = float(input('oppgi radius i cm: '))
areal = 3.14*r**2
areal2 = 3.14*r*2*r*2
omkrets = 3.14*r*2
print('arealet av sirkelen er: ', areal)
print('omkretsen av sirkelen er: ', omkrets)
print('arealet av sirkelen med dobblet radius:', areal2, 'forhold:', areal2/areal)













