n = int(input('Digite um número inteiro positivo:'))
x = 1
while x <= n:
    x += 1
    if x % 14 == 0:
        print(x)