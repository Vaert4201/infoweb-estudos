positivos = 0
negativos = 0
zeros = 0

for i in range(10):

    n = int(input())

    if n > 0:

        positivos += 1

    elif n < 0:

        negativos += 1

    else:
        zeros += 1

print()
print(f'Positivos: {positivos}')
print(f'Negativos: {negativos}')
print(f'Zeros: {zeros}')




