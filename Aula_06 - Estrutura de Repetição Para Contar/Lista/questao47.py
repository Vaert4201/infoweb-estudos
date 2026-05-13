import random

x = random.randint(1,100)

while True:
    chute = int(input('Digite qualquer número inteiro:'))

    if chute < 0 or chute > 100:
        print('Número inválido! Tente um número entre 1 e 100.')

    elif chute < x:
        print('Muito baixo!')

    elif chute > x:
        print('Muito alto!')

    elif chute < 0 or chute > 100:
        print('Número inválido! Tente um número entre 1 e 100.')
        
    else:
        print('Acertou!')
        break

