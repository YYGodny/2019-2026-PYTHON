from math import log





def f(t):
    return 2-log(t)

def b(t):
    return (log(t)-2)/(1/-t)

def areal(x):
    return (f(x)*b(x))/2


step = 0.1
stepm = 0
a = 0
while step <= 3:
    if areal(step) > a:
        a = areal(step)
        print(round(b(step)), round(f(step)))
        stepm = step
    step += 0.1

print(round(stepm))
