peso = float(input('Digite o seu peso:'))
altura = float(input('Digite a sua altura:'))
IMC = peso / (altura ** 2)
if IMC < 18.5:
    print('Abaixo do peso.')
elif 18.5 <= IMC < 25:
    print('Peso normal.')
elif 25 <= IMC < 30:
    print('Sobrepeso.')
elif IMC >= 30:
    print('Obesidade.')