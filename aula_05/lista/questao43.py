idade = int(input('Digite a idade do telespectador:'))
if idade <= 5:
    print('Gratuito.')
elif 6 <= idade <= 12:
    print('R$ 12,00')
elif 13 <= idade <= 17:
    print('R$ 18,00')
else:
    print('R$25,00')