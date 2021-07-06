d = int(input('Quantos dias alugados? '))
k = float(input('Quantos Km rodados? '))
p = (d * 60) + (k * 0.15)
print(f'O total a pagar é de R${p:.2f}')
