num1, num2 = map(float, input('Digite dois números:') .split())
op = input('Digite qualquer operador:')
if  op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif  op == '*':
    print(num1 * num2)
elif op == '/':
    if num2 == 0:
        print('Erro! Divisão por zero...')
    else:
        print(num1 / num2)
else:
    print('Operador inválido.')