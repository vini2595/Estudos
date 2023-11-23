'''

Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A

'''

total_aluno = 1
saida = 'Ss'
while saida != 'Nn':
    aluno = str(input('Digite o teu nome: '))

    questao = 1
    while questao <= 10:
        resp = str(input(f'Qual foi a resposta da {questao}ª questão? ')).strip().upper()[0]
        questao += 1

    print('-' * 35)
    saida = str(input('Outro aluno irá utilizar o programa? ')).strip().upper()[0]
    if saida == 'N':
        break

    total_aluno = int(aluno) + 1

print('Programa encerrado!')
print(f'Total de alunos: {total_aluno}')


