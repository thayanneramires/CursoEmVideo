pessoas = {'nome': 'Thayanne', 'sexo': 'F', 'idade': 20}
pessoas['nome'] = 'Thais'    # Modificação
for k, v in pessoas.items():
    print(f'{k} = {v}')
