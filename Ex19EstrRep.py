lista = []
resp = 'S'
while True:
    numero = lista.append(int(input('Digite um número: ')))
    if numero 
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp not in 'S':
        break
    print('*' * 50)
print('=' * 50)
print('Números do conjunto N:', end=' ')
for i in lista:
    print(i, end=' ')
print()
print(f'Menor número digitado: {min(lista)}\n'
      f'Maior número digitado: {max(lista)}\n'
      f'Soma de todos os números digitados: {sum(lista)}')