def area(larg, compr):
    resultado = larg * compr
    print(f'A área de um terreno {larg}x{compr} é de {resultado}m².')


# Programa principal
print(' Controle de terrenos')
print('-' * 20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
