while True:
    nota = float(input('Digite um valor entre 0 e 10: '))
    if 0 <= nota <= 10:
        print(f'Você digitou o número {nota}')
        break
    else:
        print('Valor inválido!')
        print('-' * 35)

print('-' * 35)
print('Programa finalizado')

