a = int(input('\033[33mPrimeiro valor: '))
b = int(input('\033[33mSegundo valor: '))
c = int(input('\033[33mTerceiro valor: '))

# verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'\033[34mO menor valor digitado foi \033[32m{menor}')
print(f'\033[34mO maior valor digitado foi \033[32m{maior}')
