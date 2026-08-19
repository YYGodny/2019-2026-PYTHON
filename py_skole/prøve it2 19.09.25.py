#oppgave 1
print('oppgave 1')
[print(i) for i in range(1, 41) if i % 2 == 0]
#oppgave 2
print('oppgave 2')
print(max(map(int, input('skriv inn to tall separert med komma: ').split(','))))
#oppgave 3
print('oppgave 3')
[print(f'{i}\n') for i in ['hei', 'jeg', 'er', 'bak', 'deg']]
#oppgave 4######
print('oppgave 4')
ordd = []
def f(k=''): f(ordd.append(x)) if (x:= input('skriv et ord ("stopp" for stopp):')) != 'stopp' else print(ordd)
f()
#oppgave 5
print('oppgave 5')
def f(): [print(i) for i in range(1, 41) if i % 2 != 0]
#oppgave 6
print('oppgave 6')
def sjekk_vokal(o): return True if 'a' in o and 'e' in o and 'i' in o else False
print(f'inneholder seilas aei? {sjekk_vokal("seilas")}')
#oppgave 7 ########
print('oppgave 7')
d = {}
def kvadrer(n):
    for i in range(1, n+1):
        d[i] = i**2
kvadrer(20)
[print(d[i]) for i in d]
#oppgave 8
print('oppgave 8')
def multipliser_ordbok(ordbok):
    s = 1
    for i in ordbok:
        s *= ordbok[i]
    return s
print(f'verdier av alt i ordboken multiplisert: {multipliser_ordbok(d)}')
#oppgave 9
print('oppgave 9')
print(list(set([i for i in [1, 2, 3,3, 3, 4, 4] if i in [2, 5, 3, 9, 3, 3, 10, 11, 1, 9]])))
#oppgave 10
print('oppgave 10')
print(True if len((x:= input('skriv passordet: '))) > 6 and len(x) < 18 and any([True for i in x if i in '#%!']) and any([True for i in x if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']) and any([True for i in x if i in 'abcdefghijklmnopqrstuvwxyz']) else False)

#print(oppgave) telles ikke som en linje!!!
