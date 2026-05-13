n = int(input('Digite a quantidade de degraus que você quer:'))
if n <= 0:
    print('Número inválido!')
else:
    x = 1
    while x <= n:
        print('*' * x)
        x += 1