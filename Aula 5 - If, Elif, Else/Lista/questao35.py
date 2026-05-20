vel = float(input('Digite a velocidade do seu carro:'))
if vel <= 80:
    print('Sem multa.')
elif 80 < vel <= 100:
    print('Multa leve: R$ 130')
elif 100 < vel <= 120:
    print('Multa média: R$ 195')
elif vel >= 120:
    print('Multa grave: R$ 293 + suspensão')