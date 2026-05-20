n = int(input('Digite a quantidade de números que você deseja: '))

x = 0

while x < n:
    num = int(input(f'Número {x + 1}: '))
    i = num
    qtd = 0

    while i > 0:
        qtd += 1
        i //= 10
    i = num
    soma = 0
    while i > 0:
        dig = i % 10
        soma += dig ** qtd
        i //= 10
    if soma == num:
        print('Armstrong.')
    else:
        print('Não é Armstrong.')

    x += 1   


