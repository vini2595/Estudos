num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número: '))
soma = 0
if num_1 < num_2:
    for i in range(num_1, num_2):
        if i == num_1:
            continue
        soma += i
        print(i, end=' ')
else:
    for i in range(num_2, num_1):
        if i == num_2:
            continue
        soma += i
        print(i, end=' ')
print()
print(f'Soma dos números: {soma}')
