n = int(input('Digite um número: '))
soma = 0
while n > 0:
    digito = n % 10
    soma += digito
    n //= 10
print(soma)
