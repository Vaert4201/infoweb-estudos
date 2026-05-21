for i in range(99999):
    print('----MENU----')

    print('1- Somar dois números')
    print('2- Subtrair dois números')
    print('3- Sair')

    print()

    opcao = int(input('Selecione a sua opção: '))

    print()

    if opcao == 1:

        a = int(input('Número 1: '))
        b = int(input('Número 2: '))
        print(f'Resultado da soma: {a + b}')
        break

    elif opcao == 2:

        a = int(input('Número 1: '))
        b = int(input('Número 2: '))
        print(f'Resultado da subtração: {a - b}')
        break

    elif opcao == 3:

        print('Saindo....')
        break

    else:

        print('Opção inválida! Coloque uma das opções acima..')
        print()
        continue



