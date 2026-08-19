
def f(x):
    return x**2+2*x-6

def deriverte(f, a, delta_x):
    return (f(a + delta_x)-f(a))/delta_x

def nullpunkt_til_tangent(stigning, x_verdi, y_verdi):
    #formen til en tangent er y = ax+b
    #vi finner b ved å subtrahere ax på begge sider. b = y-ax
    b = y_verdi-stigning*x_verdi
    #vi finner nullpunktet ved å sette ax+b lik 0
    #slik: 0 = ax+b
    #vi finner x ved å subtrahere b og dele med a. x = -b/a
    return round(-b/stigning, 2)


start_verdi = 7


for i in range(10):
    print(nullpunkt_til_tangent(deriverte(f, start_verdi, 0.00001), start_verdi, f(start_verdi)))
    start_verdi = nullpunkt_til_tangent(deriverte(f, start_verdi, 0.00001), start_verdi, f(start_verdi))


