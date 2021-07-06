from random import choice

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
lista = [n1, n2, n3]
escolhido = choice(lista)
print(f'O aluno escolhido foi {escolhido}')
