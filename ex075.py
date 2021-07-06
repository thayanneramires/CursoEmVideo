tot18 = toth = totm20 = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo in 'F' and idade < 20:
        totm20 += 1
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print(f'''Total de pessoas com mais de 18 anos : {tot18}
Ao todo temos {toth} homens cadastrados
E {totm20} mulheres com menos de 20 anos''')
