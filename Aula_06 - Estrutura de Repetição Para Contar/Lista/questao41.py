n = int(input('Quantos pares diferentes você deseja digitar?'))
contador = 1
while contador <= n:
    a = int(input(f'Digite o primeiro número do par {contador}:'))
    b = int(input(f'Digite o segundo número do par {contador}:'))
    if a > b:
        print(f'{a} é maior que {b}')
    elif a < b:
        print(f'{a} é menor que {b}')
    else:
        print(f'{a} é igual a {b}')

        print()
        
    contador += 1