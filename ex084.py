num = [2, 5, 9, 1]
num[1] = 6
num.append(4)
num.sort(reverse=True)
num.insert(2, 7)
num.pop(2)
del num[0]
if 8 in num:
    num.remove(8)
else:
    print('Não achei o número 8')

print(num)
print(f'Essa lista tem {len(num)} elementos')
