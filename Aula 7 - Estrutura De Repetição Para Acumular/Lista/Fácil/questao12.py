n = int(input('Digite o seu número: '))

while n > 0:
    digito = n % 10
    print(digito, end='')
    n //= 10