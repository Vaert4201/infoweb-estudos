
numeros = []

for i in range(9999):
    
    n = int(input())

    if n < 0:
        break

    numeros.append(n)

print(sum(numeros))
