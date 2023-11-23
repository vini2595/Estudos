while True:
    nome = str(input('Nome de usuário: '))
    senha = str(input('Senha: '))
    if nome != senha:
        break
    else:
        print('Senha não pode ser igual ao nome do usuário!')
        print('-' * 50)

print('*' * 35)
print('Programa finalizado')

