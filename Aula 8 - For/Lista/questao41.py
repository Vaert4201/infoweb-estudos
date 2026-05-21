n = int(input())

for i in range(n):

    a = int(input())
    b = int(input())

    if a > b:
        print(f'Maior: {a}')
        print(f'Menor: {b}')
    
    elif a < b:
        print(f'Maior: {b}')
        print(f'Menor: {a}')

    else:
        print(f'{a} e {b} são iguais.')

    