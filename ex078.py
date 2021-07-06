contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
            'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
            'doze', 'treze', 'catroze', 'quinze', 'dezesseis',
            'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 a 20: '))
    if 0 < n > 20:
        print('Tente novamente.', end=' ')
    else:
        print(f'Você digitou o número {contagem[n]}')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
