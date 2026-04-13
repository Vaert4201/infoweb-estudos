mes = int(input('Digite qualquer número:'))
if mes in [1, 3, 5, 7, 8, 10, 12]:
    print('O mês tem 31 dias.')
elif mes in [4, 6, 9, 11]:
    print('O mês tem 30 dias.')
elif mes == 2:
    print('O mês tem 28 dias.')
else:
    print('Mês inválido.')