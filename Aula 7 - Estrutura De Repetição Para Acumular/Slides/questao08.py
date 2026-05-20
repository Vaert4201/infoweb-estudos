n = int(input('Digite qualquer número inteiro positivo:'))
x = 1
soma = 0
while x <= n:
    if x % 3 == 0:
        soma += x
    x += 1
print(f'Soma dos múltiplos de 3: {soma}')