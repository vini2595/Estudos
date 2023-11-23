lista = []
for x in range(5):
    lista.append(int(input(f'Digite o {x + 1}º número: ')))
print('=' * 30)
print(f'O maior número digitado foi {max(lista)}')