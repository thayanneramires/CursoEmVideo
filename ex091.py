numlist = []
par = []
impar = []
while True:
    numlist.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
for i, v in enumerate(numlist):
    if v % 2 == 0:
        par.append(v)
    if v % 2 == 1:
        impar.append(v)
print('-='*30)
print(f'A lista completa é {numlist}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
