estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Uidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())  # fazer uma cópia  # fatiamento dos dados
'''for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')'''
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
