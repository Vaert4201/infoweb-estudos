
n = int(input())

maior = float('-inf')

print()

for i in range(n):

    nota = float(input())

    if nota > maior:

        maior = nota
print()

print(maior)
