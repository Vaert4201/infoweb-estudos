peso = float(input('Digite o seu peso:'))
altura = float(input('Digite a sua altura:'))
IMC = peso / (altura ** 2)
if IMC < 25:
    print('Peso normal.')
else:
    print('Acima do peso.')
