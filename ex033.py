from datetime import date
ano = int(input('\033[31mQue ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\033[31mO ano \033[33m{ano} \033[31mé BISSEXTO!')
else:
    print(f'\033[31mO ano \033[33m{ano} \033[31mnão é BISSEXTO!')
