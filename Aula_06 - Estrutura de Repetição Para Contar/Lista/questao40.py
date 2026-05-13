n = int(input('Digite um número inteiro positivo:'))
x = 1
soma = 0
while x < n:
    if n % x == 0:
        soma += x
    x += 1

if soma == n:
    print('O número é perfeito!')
else:
    print('O número não é perfeito!')
