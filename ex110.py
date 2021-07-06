jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

print('=' * 40)
print('Cod ', end='')            # cabeçalho
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')   # str porque pode ser numérico
    print()
while True:
    print('-' * 40)
    opc = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if opc == 999:
        break
    if opc >= len(time):
        print(f'ERRO! Não existe jogador com código {opc}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[opc]["nome"]}: ')
        for i, g in enumerate(time[opc]["gols"]):
            print(f'No jogo {i + 1} fez {g} gols.')
print('<< VOLTE SEMPRE >>')
