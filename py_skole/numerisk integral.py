from math import e
a = 0 #start
b = 1 #slutt
n = 1000
dx = (b-a)/n

def f(x):
    return 100/(1+2*e**(-0.05*x))

def venstre_integral():
    s = 0
    for i in range(n):
        s += f(a+dx*i)*dx
    return s

def høyre_integral():
    s = 0
    for i in range(n):
        s += f(a+dx*(i+1))*dx
    return s

def midt_integral():
    s = 0
    for i in range(n):
        s += f(a+dx*(i-0.5))*dx
    return s

def trapes_integral(slutt='s'):
    s = 0
    if slutt == 's':
        for i in range(n):
            s += ((f(a+dx*(i+1))+f(a+dx*i))/2)*dx
    else:
        dxx = (slutt-a)/n
        for i in range(n):
            s += ((f(a+dxx*(i+1))+f(a+dxx*i))/2)*dxx
    return s

for i in range(-100, 200):
    if trapes_integral(i) > 9900 and trapes_integral(i) < 10000:
        b = i
for i in range(100):
    b += 0.01
    if round(trapes_integral(b)) == 9999:
        print(trapes_integral(b), b)
        
print(venstre_integral())
print(høyre_integral())
print(midt_integral())
print(trapes_integral())
