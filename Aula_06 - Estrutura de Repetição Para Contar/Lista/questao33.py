n = int(input('Digite um número inteiro:'))
soma_pares = 0
soma_impares = 0
contador = 1
while n != 0:
    contador += 1
    n = int(input('Digite qualquer outro número inteiro:'))
    if n % 2 == 0:
        soma_pares += n
    else:
        soma_impares += n
print(f'Soma dos pares: {soma_pares}')
print(f'Soma dos impares: {soma_impares}')
