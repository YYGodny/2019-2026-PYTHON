a = -10
b = 10

def f(x):
    return x**2-5

m = (a+b)/2

while abs(f(m)) >= 0.00001:
    if f(a)*f(m) < 0:
        b = m
    else:
        a = m

    m = (a+b)/2
    
print(m)


