a = b = 1
c = 0
cont = 1
print('Sequência de Fibonacci: ', end=' ')
print(a, end=' ')
print(b, end=' ')

while True:
    c = a + b
    print(c, end=' ')
    b = a
    a = c
    if c >= 500:
        break



