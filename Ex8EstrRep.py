lista = []
for x in range(5):
    lista.append(int(input(f'Digite o {x + 1}º número: ')))
print('=' * 40)
print(f'O maior número digitado foi {sum(lista)}')
print(f'A média dos números digitados é {sum(lista) / len(lista)}')