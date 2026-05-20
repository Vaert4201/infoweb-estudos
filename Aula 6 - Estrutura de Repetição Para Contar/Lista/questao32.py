n = int(input('Digite um número inteiro positivo:'))
x = 1
while x <= n:
    if n % x == 0:
        print(x)
    x += 1
    