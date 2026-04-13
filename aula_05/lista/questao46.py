num1, num2 = map(int, input('Digite dois números inteiros:') .split())
op = input('Digite uma operação:')
if op == max:
    print(max = (num1, num2))
elif op == min:
    print(min = (num1, num2))
elif op == '+':
    print(num1 + num2)
elif op == '-':
    print((num1 - num2))
else:
    print('Opção inválida.')
