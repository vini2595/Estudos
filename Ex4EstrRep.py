A = 80000
B = 200000
t = 0
while A <= B:
    A = A + 0.03 * A
    B = B + 0.015 * B
    t += 1

print('*' * 35)
print(f'O tempo necessário para que o país A ultrapasse ou iguale ao país B é {t} anos')