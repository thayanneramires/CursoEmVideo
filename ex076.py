totp = totpmaisdmil = cont = valorpbarato = 0
pmaisbarato = ' '
print('-' * 40)
print(f'{"LOJA SUPER BARATÃO":^40}')
print('-' * 40)
while True:
    produto = str(input('Nome do Produto: '))
    valor = float(input('Preço: R$'))
    cont += 1
    totp += valor
    if valor >= 1000:
        totpmaisdmil += 1
    if cont == 1 or valor < valorpbarato:
        pmaisbarato = produto
        valorpbarato = valor
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{" FIM DO PROGRAMA ":-^40}')
print(f'''O total da compra foi R${totp:.2f}
Temos {totpmaisdmil} produtos custando mais de R$1000.00
O produto mais barato foi {pmaisbarato} que custa R${valorpbarato:.2f}''')
