m = int(input('skriv et tall: '))
s = 0
for i in range(0, m + 1, 2):
    print(i)
    s += i
print(f'summen er {s}')