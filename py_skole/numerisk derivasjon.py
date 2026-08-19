
def f(x):
    return x**2-6

def deriverte(f, a, delta_x):
    return round((f(a + delta_x)-f(a))/delta_x, 3)

dx = 0.000001

print(f'den deriverte av funksjonen i punkt 2 er {deriverte(f, 2, dx)}')


