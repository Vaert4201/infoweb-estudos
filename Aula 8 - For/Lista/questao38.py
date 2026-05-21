n = int(input())

maior = float('-inf')
menor = float('inf')

print()

for i in range(n):

    num = int(input())

    if num > maior:

        maior = num
    
    if num < menor:

        menor = num

print()
print(maior)
print(menor)
