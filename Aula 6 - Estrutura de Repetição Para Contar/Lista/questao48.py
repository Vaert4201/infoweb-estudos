n = int(input('Digite o seu número inteiro positivo: '))
invertido = 0
original = n

while n > 0:
    digito = n % 10
    invertido = invertido * 10 + digito
    n = n // 10
if original == invertido:
    print('Palindromo Numerico')
else:
    print('Não é um palindromo numerico')
