a = b = 1
c = 0
cont = 1
print('Sequência de Fibonacci: ', end=' ')
print(a, end=' ')
print(b, end=' ')

while cont < 10:
    c = a + b
    print(c, end=' ')
    b = a
    a = c


