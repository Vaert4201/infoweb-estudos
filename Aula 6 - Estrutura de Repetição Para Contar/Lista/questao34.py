a = int(input('Digite um número inteiro:'))
b = int(input('Digite outro número inteiro:'))

while b != 0:
    resto = a % b
    a = b
    b = resto
print(f'MDC: {a}')