inicio = int(input())
fim = int(input())

soma = 0

print()

for n in range(inicio, fim + 1):

    if n < 2:
        continue

    primo = True

    for i in range(2, n):

        if n % i == 0:

            primo = False
            break

    if primo:

        soma += n

print(f'A soma dos números primos são: {soma}')


