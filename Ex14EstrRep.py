pares = []
impares = []
lista = []

for i in range(10):
    lista.append(int(input(f'Digite o {i + 1}º número: ')))
    if lista[i] % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print('=' * 70)
print(f'Total de pares e ímpares digitados foram, respectivamente, {len(pares)} e {len(impares)}')
