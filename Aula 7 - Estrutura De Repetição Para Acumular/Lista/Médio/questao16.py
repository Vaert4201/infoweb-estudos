n = int(input('Digite o seu número: '))
passos = 0
print('Sequência:', end=' ')

while True:
    print(n, end=' ')

    if n == 1:
        break

    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    
    passos += 1
print()
print(f'Passos: {passos}')

    