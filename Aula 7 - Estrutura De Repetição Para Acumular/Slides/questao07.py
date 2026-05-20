n = int(input('Digite qualquer número inteiro positivo:'))
x = 1
prod = 1
while x <= n:
    prod *= x
    x += 1
print(f'Produto: {prod}')