n = int(input('Digite o denominador da última fração:'))
soma = 0
x = 1
while x <= n:
    soma += 1 / x
    x += 1
print(soma)