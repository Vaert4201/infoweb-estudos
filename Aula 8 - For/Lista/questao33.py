soma_pares = 0
soma_impares = 0

for i in range(9999):

    n = int(input())

    if n == 0:
        
        break

    if n % 2 == 0:

        soma_pares += n

    else:

        soma_impares += n

print()

print(f'Soma dos pares: {soma_pares}')
print(f'Soma dos ímpares: {soma_impares}')