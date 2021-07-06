from datetime import date

sexo = int(input('Se você for homem digite 1 ou se for mulher digite 2: '))
if sexo == 1:
    print('O alistamento é obrigatório para você.')
    nasc = int(input('Ano do nascimento: '))
    atual = date.today().year
    idade = atual - nasc
    print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        tempo = 18 - idade
        print(f'Ainda falam {tempo} anos para o alistamento.')
        ano = atual + tempo
        print(f'Seu alistamento será em {ano}.')
    elif idade > 18:
        tempo = idade - 18
        print(f'Já deveria ter se alistado há {tempo} anos.')
        ano = atual - tempo
        print(f'Seu alistamento foi em {ano}.')
elif sexo == 2:
    print('Você não é obrigada a fazer o alistamento')
