
qtd_pares = 0
qtd_impares = 0

for i in range(9999):

    n = int(input())

    if n < 0:

        break

    if n % 2 == 0:

        qtd_pares += 1

    else:

        qtd_impares += 1


print(f'Quantidade de números pares: {qtd_pares}')
print(f'Quantidade de números ímpares: {qtd_impares}')
