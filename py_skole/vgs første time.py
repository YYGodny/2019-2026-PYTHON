iphone = 11000
innskudd = 8000
rente = 0.003

saldo = innskudd
måneder = 0

while saldo < iphone:
    saldo = saldo + saldo*rente
    måneder += 1

print(f'det tok {måneder} måneder')

