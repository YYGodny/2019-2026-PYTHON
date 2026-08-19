figurtall = 20
tilsammen = 0

for n in range(1, figurtall+1):
    fyrstikker = 5*n+1
    tilsammen += fyrstikker
    print(fyrstikker, n, tilsammen)
print(f'du trenger {tilsammen} fyrstikker for å lage de 20 første figurene')
