while True:
    valor = int(input('Tabuada de qual número deseja ver? '))
    if not 1 < valor < 10:
        print('O valor tem que ser entre 1 e 10')
        break
    else:
        print('=' * 40)
        cont = 1
        print(f'Tabuada de {valor}: ')
        while cont <= 10:
            print(f'{valor} x {cont} = {valor * cont}')
            cont += 1
        break
