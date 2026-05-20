n = int(input('Digite o seu número: '))

it = 0

while n >= 10:

    soma = 0

    while n > 0:
        dig = n % 10
        soma += dig
        n //= 10

    n = soma
    it += 1

print(f'Raiz: {n}')
print(f'Interações: {it}')