import random

n = random.randint(1, 100)

for i in range(99999):

    num = int(input())

    if num < n:

        print('Muito baixo!')

    elif num > n:

        print('Muito alto!')

    else:

        print('Acertou!')
        break



