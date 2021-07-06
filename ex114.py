def contador(* num):    # desempacotar
    for valor in num:
        print(f'{valor}', end='')
    print()


contador(1, 5, 8)
contador(4, 0)
contador(4, 8, 7, 5)



'''def contador(* num):
    tam = len(num)
    print(f'Recebi os valore {num} e são ao todo {tam} números')


contador(1, 5, 8)
contador(4, 0)
contador(4, 8, 7, 5)'''
