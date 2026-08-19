def f(x):
    return 2**x
for i in range(6):
    a = f(i)
    b = f(i+1)
    print(a)
    print(f'forskjell: {b-a}, prosent: {100/(a/b)}')
    print(b)

