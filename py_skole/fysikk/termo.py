#oppgave 1
k = 1.38E-23
u = 1.66E-27
 
T = 298.15
U1 = (5/2)*k*T
U2 = (3/2)*k*T
mN2= 14.01*2*u
 
v = round(((2*U2)/mN2)**.5)
print(f"{U1}J")
print(f'{v}m/s')
 
#oppgave 2
 
m2 = 3000 #g
romtemperatur = 298.15 #K
kokepunkt = 77.35 #K
T = romtemperatur - kokepunkt
cpN2 = 1.040 #J/(g*K)
fordampingsvarmeN2 = 200 #J/g
 
EnergiN2 = T*cpN2*m2 + m2*fordampingsvarmeN2
 
print(f'{EnergiN2}J')


#oppgave 3
mH2O = 200
cpH2Og = 2.08
cpH2Ol = 4.18
fordampningsvarme = 2265
smeltevarme = 334
molekylmasse_H2O = (2*1.008+16)*u #kg

restenergi = EnergiN2-(fordampningsvarme+smeltevarme+cpH2Ol*mH2O*100)

print(restenergi/(mH20*cpH2Og))

