from random import randint
computer = randint(0, 10)
print('''Sou seu computador... Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
acertou = False
palpites = 0
while not acertou:
    player = int(input('Qual é seu palpite? '))
    palpites += 1
    if player == computer:
        acertou = True
    else:
        if player < computer:
            print('Mais... Tente mais uma vez.')
        if player > computer:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')
