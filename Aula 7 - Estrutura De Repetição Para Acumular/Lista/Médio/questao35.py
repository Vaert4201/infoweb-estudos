n = int(input('Digite o seu número: '))

div = 2
maior = 1


while n > 1:

    while n % div == 0:
        maior = div
        n //= div

    div += 1

print(maior)