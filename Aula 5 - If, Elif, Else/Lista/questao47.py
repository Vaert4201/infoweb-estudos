num = int(input('Digite qualquer número inteiro:'))
if 0 <= num <= 49:
    print('Insuficiente.')
elif 50 <= num <= 69:
    print('Regular')
elif 70 <= num <= 89:
    print('Bom')
elif 90 <= num <= 100:
    print('Excelente.')
else:
    print('Nota inválida.')