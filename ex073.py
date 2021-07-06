while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-' * 30)
    for cont in range(1, 11):
        print(f'{n} x {cont:2} = {n * cont}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
