n = int(input('Digite o número inteiro positivo: '))
x = n
invertido = 0

while n > 0:
    dig = n % 10
    invertido = invertido * 10 + dig
    n //= 10

if x == invertido:
    print('Palíndromo.')
else:
    print('Não é palíndromo.')