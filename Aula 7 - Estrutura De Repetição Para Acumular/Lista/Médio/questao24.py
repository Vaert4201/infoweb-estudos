n = int(input('Digite o seu número: '))
k = 0

if n < 0:
    print('Valor inválido.')
else:
    while (k + 1) * (k + 1) <= n:
        k += 1
print(k)
