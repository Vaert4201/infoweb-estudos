n = int(input('Digite a quantidade de números: '))
pares = 0
impares = 0
contador = 0
while contador < n:
    num = int(input(f'Número {contador + 1}: '))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    contador += 1
print(f'Pares: {pares}')
print(f'Impares: {impares}')