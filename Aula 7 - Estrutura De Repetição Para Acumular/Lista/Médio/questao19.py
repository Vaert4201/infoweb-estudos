n = int(input('Digite o seu número: '))

if n == 0:
    print('0')
elif n < 0:
    print('Não existe número binário para número negativo.')
else:
    binario = ''

    while n > 0:
        resto = n % 2
        binario = str(resto) + binario
        n = n // 2
    print(binario)
