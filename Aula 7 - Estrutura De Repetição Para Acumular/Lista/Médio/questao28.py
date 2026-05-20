n = int(input('Digite o seu número: '))

per = 0

while n >= 10:
    
    prod = 1

    while n > 0:
        dig = n % 10
        prod *= dig
        n //= 10

    n = prod
    per += 1

print(f'Persistência: {per}')