casa = float(input('Valor da casa: R$'))
salario = float(input('Sálario do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

print(f'Para pagar uma casa de {casa:.2f} em {anos} anos', end='')
print(f' a prestação será de {prestacao:.2f}')
print('Empréstimo pode ser CONCEDIDO!' if prestacao <= minimo else 'Empréstimo NEGADO!')
