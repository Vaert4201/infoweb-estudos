n = int(input('Digite o seu número: '))
if n <= 1:
    print('Não é primo.')
else:
    x = 2

    while x * x <= n:
        if n % x == 0:
            print('Não é primo')
            break
        x += 1
    else:
        print('É primo')