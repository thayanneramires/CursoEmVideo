print(f'\033[34m{" LOJAS RAMIRES ":=^40}')
preco = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('''[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão')
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = preco / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')
elif opcao == 4:
    vezes = int(input('Quantas parcelas? '))
    total = preco + (preco * 20 / 100)
    parcela = total / vezes
    print(f'Sua compra será parcelada em {vezes}x de R${parcela:.2f} COM JUROS')
else:
    total = preco
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente.')
print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')
