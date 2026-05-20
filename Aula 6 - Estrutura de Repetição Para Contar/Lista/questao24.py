n = int(input('Digite um número inteiro:'))
soma = 0
while n > 0:
    digitos = n % 10
    soma += digitos
    n //= 10
print(f'Soma dos digitos: {soma}')