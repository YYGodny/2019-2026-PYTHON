A1 = ''
A2 = ''
A3 = ''
B1 = ''
B2 = ''
B3 = ''
C1 = ''
C2 = ''
C3 = ''
board = f'1:   {A1} | {B1}  | {C1} \n   -----------\n2:   {A2} | {B2}  | {C2} \n   -----------\n3:  {A3}  | {B3}  | {C3}\n\n    A   B  C'

print(board)
while True:
    x1 = input('player1: ').lower()
    x2 = input('player2: ').lower()
    if x1 == x2:
        print('dere er dumme')
    
