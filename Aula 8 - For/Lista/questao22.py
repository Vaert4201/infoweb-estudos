n = int(input())

menor = float('inf')

print()

for i in range(n):

    nota = float(input())

    if nota < menor:

        menor = nota

print()

print(menor)


