def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2        # receber o dobro
        pos += 1


valores = [5, 5, 6, 3, 9]
dobra(valores)
print(valores)
