n = int(input('Digite qualquer número inteiro:'))
contador_pares = 0
contador_impares = 0


while n > 0:
    n = int(input('Digite outro número inteiro:'))
    if n % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1
print(f'Quantidade de números pares: {contador_pares}')
print(f'Quantidade de números impares: {contador_impares}')    

