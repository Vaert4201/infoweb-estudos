opcao = 0

while opcao != 3:
    print('MENU:')
    print('1- Somar os dois números:')
    print('2- Subtrair os dois números:')
    print('3- Sair')

    opcao = int(input('Selecione sua opção:'))

    if opcao == 1:
        a = float(input('Digite o seu número inteiro:'))
        b = float(input('Digite o seu outro número inteiro:'))
        print(f'Soma: {a + b}')
    elif opcao == 2:
        a = float(input('Digite o seu número inteiro:'))
        b = float(input('Digite o seu outro número inteiro:'))
        print(f'Subtração: {a - b}')
    elif opcao == 3:
        print('Saindo do programa...')
    else:
        print('Opção inválida. Selecione uma opção válida.')