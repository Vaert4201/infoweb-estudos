a, b = map(int, input('Digite os seus dois números: ') .split())

n = a
qtd = 0


while n <= b:

    if n >= 2:

        div = 1
        qtd = 0

        while div <= n:

            if n % div == 0:
                qtd += 1
            
            div += 1

        if qtd == 2:
            print(n)
            qtd += 1
    n += 1

print(f'Quantidade de primos: {qtd}')

