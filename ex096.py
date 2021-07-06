num = [[], []]
for n in range(1, 8):
    numero = int(input(f'Digite o {n}° valor: '))
    if numero % 2 == 0:
        num[0].append(numero)
    if numero % 2 == 1:
        num[1].append(numero)
print('=-' * 30)
num[0].sort()
print(f'Os valores pares digitados foram: {num[0]}')
num[1].sort()
print(f'Os valores ímpares digitados foram: {num[1]}')
