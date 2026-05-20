n = int(input('Digite a quantidade de números: '))
maior = float('-inf')
menor = float('inf')

while n > 0:
    num = int(input(f'Número: '))

    if num > maior:
        maior = num
    
    if num < menor:
        menor = num
    n -= 1

print(f'Maior: {maior}')
print(f'Menor: {menor}')