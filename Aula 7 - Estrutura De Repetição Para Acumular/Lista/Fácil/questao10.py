n = int(input('Digite a quantidade de termos da sequência: '))

x = 0
y = 1
z = 0

while z < n:
    print(x, end=' ')
    prox = x + y
    x = y
    y = prox

    z += 1