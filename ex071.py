r = 'S'
c = soma = media = maior = menor = 0
while r in 'S':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    c += 1
    soma += n
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / c
print(f'Você digitou {c} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
