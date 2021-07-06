salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f'Quem ganhava R$\033[31m{salario:.2f}\033[m passa a genhar R$\033[33m{novo:.2f}\033[m agora.')
