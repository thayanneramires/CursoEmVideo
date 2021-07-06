valores = list()
for cont in range(1, 6):
    valores.append(int(input(f'Digite o {cont}° valor: ')))
for c, v in enumerate(valores):  # encontrar a posição/index
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')
