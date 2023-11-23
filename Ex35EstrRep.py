n = int(input("Digite um número inteiro qualquer: "))
mult = 1
primos = []
for count in range(1, n):
    if count % count == 0:
        primos.append(count)

print(primos)
