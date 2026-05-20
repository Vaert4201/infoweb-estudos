contador = 1
positivos = 0
negativos = 0
zeros = 0
while contador <= 10:
    n = int(input('Digite um número inteiro:'))
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1
    else:
        zeros += 1
    contador += 1
print(f'Quantidade de números positivos: {positivos}')
print(f'Quantidade de números negativos: {negativos}')
print(f'Quantidade de zeros: {zeros}')
