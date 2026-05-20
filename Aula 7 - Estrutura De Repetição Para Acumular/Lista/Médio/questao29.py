soma = 0
total = 0
positivos = 0

while soma <= 1000:

    n = int(input())

    total += 1

    if n > 0:
        soma += n
        positivos += 1

print(f'Total lidos: {total}')
print(f'Positivos: {positivos}')