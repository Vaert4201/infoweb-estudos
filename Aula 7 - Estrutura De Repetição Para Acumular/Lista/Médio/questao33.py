n = int(input('Digite a quantidade de termos da sequência: '))

a = 1
b = 1
c = 1

x = 0

while x < n:

    if x == 0 or x == 1 or x == 2:
        print(1, end=' ')
    else:
        prox = a + b
        print(prox, end=' ')

        a = b
        b = c
        c = prox

    x += 1