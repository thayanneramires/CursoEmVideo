print('=' * 40)
print(f'{" 10 TERMOS DE UMA PA ":^40}')
print('=' * 40)
t1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = t1 + (10 - 1) * r
for c in range(t1, decimo + r, r):
    print(c, end=' → ')
print('Acabou')
