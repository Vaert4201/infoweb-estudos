n = int(input('Digite a quantidade de números inteiros:'))
contador = 1
soma_positivos = 0
soma_negativos = 0
while contador <= n:
    x = int(input(f'Número {contador}:'))
    if x >= 0:
        soma_positivos += x
    else:
        soma_negativos += x
    contador += 1
print(f'Soma dos números positivos: {soma_positivos}')
print(f'Soma dos números negativos: {soma_negativos}')
