#Leia um número inteiro. Se ele for múltiplo de 5, exiba "Múltiplo de 5".

mult = int(input('Digite qualquer número inteiro:'))

if mult % 5 == 0:
    print('Múltiplo de 5.')
else:
    print('Não é multiplo de 5.')