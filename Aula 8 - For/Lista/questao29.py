n = int(input())

soma_positivos = 0

soma_negativos = 0

print()

for i in range(n):

    num = int(input())

    if num > 0:
        
        soma_positivos += num

    else:
        
        soma_negativos += num
print()

print(f'Soma dos positivos: {soma_positivos}')
print(f'Soma dos negativos: {soma_negativos}')
