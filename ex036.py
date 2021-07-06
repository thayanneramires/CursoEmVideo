print('\033[1;35m-=-' * 10)
print('\033[1;34mAnalisador de Triângulos')
print('\033[1;35m-=-' * 10)
r1 = float(input('\033[1;34mPrimeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[35mPODEM FORMAR\033[m \033[34mtriângulo!')
else:
    print('Os segmentos \033[35mNÃO PODEM FORMAR\033[m \033[34mtriângulo!')
