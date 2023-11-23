A = float(input('População inicial do A: '))
B = float(input('População inicial de B: '))
tx_cresc_A = float(input('Taxa anual de crescimento de A em %: '))
tx_cresc_B = float(input('Taxa anual de crescimento de B em %: '))
t = 0
while A <= B:
    A = A + (tx_cresc_A / 100) * A
    B = B + (tx_cresc_B / 100) * B
    t += 1

print('*' * 100)
print(f'O tempo necessário para que o país A ultrapasse ou iguale ao país B é {t} anos')