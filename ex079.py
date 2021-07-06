times = ('Internacional', 'Vasco', 'Atlético - MG', 'Palmeiras', 'São Paulo', 'Santos', 'Fluminense', 'Bahia', 'Grêmio',
         'Athletico - PR', 'Botafogo', 'Bragantino', 'Flamengo', 'Corinthians', 'Goiás', 'Fortaleza', 'Atlético-GO',
         'Sport', 'Ceará', 'Coritiba')
print('-='*15)
print(f'Lista de times do brasileirão: {times}')
print('-='*15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-='*15)
print(f'Os 4 últimos são {times[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética {sorted(times)}')
print('-='*15)
print(f'O Flamengo está na {times.index("Flamengo") + 1}° posição')
