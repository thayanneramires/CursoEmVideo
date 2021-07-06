real = float(input('Quanto dinheiro você tem a carteira? R$'))
dolar = real / 5.58
euro = real / 6.04
print(f'Com R${real:.2f} você pode comprar US${dolar:.2f} e {euro:.2f} em Euro')
