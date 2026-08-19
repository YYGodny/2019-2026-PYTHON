def f(x):
    return (x**3)-2*(x**2)

def integral(f, a, b):
    n = 1000
    d = (b-a)/n
    s = 0
    for i in range(n):
        s += f(d*i)*d

    return s

x = 0

while round(integral(f, 0, x), 2) != 9/4:
    x += 0.001
##    print(round(integral(f, 0, x)))
print(round(x, 1))

    
