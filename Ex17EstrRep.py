num = int(input('Digite o valor que deseja ver o fatorial: '))
cont = num
fat = 1
print('=' * 45)
print(f'{num}! =', end=' ')
while cont > 0:
    fat = fat * cont
    print(f'{cont}', end=' ')
    if cont == 1:
        print('=', end=' ')
        break
    print('x', end=' ')
    cont -= 1
print(fat)
