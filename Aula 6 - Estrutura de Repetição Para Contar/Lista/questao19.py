n = int(input('Digite a quantidade de termos da PA:'))
a = int(input('Digite o primeiro termo da PA:'))
r = int(input('Digite a razão da PA:'))
x = 1
while x <= n:
    print(a)
    a += r
    x += 1

    # O calculo da PA é feito a partir disso:
    # an = a1 + (n - 1) * r
    # onde nessa sentença daria esse resultado:
    # exemplo:
    # n = 4, a = 1, r = 8
    # a4 = 1 + (4 - 1) * 8
    # a4 = 25
    # o resultado da PA seria: 1, 9, 17, 25